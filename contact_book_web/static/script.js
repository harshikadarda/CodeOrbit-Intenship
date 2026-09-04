/*
 * Contact Book — frontend logic
 * Talks to the Flask JSON API (/api/contacts) and renders the card grid.
 * No frameworks — plain fetch + DOM.
 */

const cardGrid = document.getElementById("cardGrid");
const emptyMsg = document.getElementById("emptyMsg");
const statusMsg = document.getElementById("statusMsg");
const searchInput = document.getElementById("searchInput");

const modalOverlay = document.getElementById("modalOverlay");
const contactForm = document.getElementById("contactForm");
const modalTitle = document.getElementById("modalTitle");
const formError = document.getElementById("formError");

const fieldName = document.getElementById("fieldName");
const fieldPhone = document.getElementById("fieldPhone");
const fieldEmail = document.getElementById("fieldEmail");

const confirmOverlay = document.getElementById("confirmOverlay");
const confirmText = document.getElementById("confirmText");

let editingId = null;     // null = "add" mode, otherwise the id being edited
let pendingDeleteId = null;
let searchDebounce = null;

// Palette for the rolodex-style tab flag on each card, rotated by name hash
// so a given contact always gets the same color.
const TAB_COLORS = ["#3f6d5c", "#a2402d", "#c9a227", "#3d5a73", "#6b4c6b", "#74793f"];

function colorForName(name) {
  let hash = 0;
  for (let i = 0; i < name.length; i++) {
    hash = (hash * 31 + name.charCodeAt(i)) >>> 0;
  }
  return TAB_COLORS[hash % TAB_COLORS.length];
}

// ---------------------------------------------------------------------
// Fetching & rendering
// ---------------------------------------------------------------------
async function fetchContacts(query = "") {
  const url = query ? `/api/contacts?q=${encodeURIComponent(query)}` : "/api/contacts";
  const res = await fetch(url);
  const contacts = await res.json();
  renderContacts(contacts, query);
}

function renderContacts(contacts, query = "") {
  cardGrid.innerHTML = "";

  if (contacts.length === 0) {
    if (query) {
      emptyMsg.querySelector(".empty-title").textContent = "No matches found";
      emptyMsg.querySelector(".empty-sub").textContent = `Nothing in the box matches "${query}".`;
    } else {
      emptyMsg.querySelector(".empty-title").textContent = "No contacts yet";
      emptyMsg.querySelector(".empty-sub").textContent = "Add your first one above to start filling the box.";
    }
    emptyMsg.hidden = false;
    return;
  }
  emptyMsg.hidden = true;

  contacts.forEach((c, i) => {
    cardGrid.appendChild(buildCard(c, i));
  });
}

function buildCard(contact, index) {
  const card = document.createElement("div");
  card.className = "index-card contact-card";
  card.dataset.id = contact.id;
  card.style.animationDelay = `${Math.min(index, 12) * 35}ms`;

  const emailValue = contact.email
    ? `<span class="card-line-value">${escapeHtml(contact.email)}</span>`
    : `<span class="card-line-value empty">not provided</span>`;

  const initial = contact.name.trim().charAt(0).toUpperCase() || "?";
  const tabColor = colorForName(contact.name);

  card.innerHTML = `
    <div class="card-tab" style="background:${tabColor}">${escapeHtml(initial)}</div>
    <div class="punch-hole"></div>
    <h3 class="card-name">${escapeHtml(contact.name)}</h3>
    <div class="card-line">
      <span class="card-line-label">Phone</span>
      <span class="card-line-value">${escapeHtml(contact.phone)}</span>
    </div>
    <div class="card-line">
      <span class="card-line-label">Email</span>
      ${emailValue}
    </div>
    <div class="card-actions">
      <button class="icon-btn edit" type="button">Edit</button>
      <button class="icon-btn delete" type="button">Remove</button>
    </div>
  `;

  card.querySelector(".edit").addEventListener("click", () => openEditModal(contact));
  card.querySelector(".delete").addEventListener("click", () => openConfirmDelete(contact));

  return card;
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

// ---------------------------------------------------------------------
// Status banner
// ---------------------------------------------------------------------
function showStatus(message) {
  statusMsg.textContent = message;
  statusMsg.hidden = false;
  clearTimeout(showStatus._t);
  showStatus._t = setTimeout(() => { statusMsg.hidden = true; }, 3200);
}

// ---------------------------------------------------------------------
// Add / Edit modal
// ---------------------------------------------------------------------
function openAddModal() {
  editingId = null;
  modalTitle.textContent = "New contact";
  contactForm.reset();
  formError.hidden = true;
  modalOverlay.hidden = false;
  fieldName.focus();
}

function openEditModal(contact) {
  editingId = contact.id;
  modalTitle.textContent = "Edit contact";
  fieldName.value = contact.name;
  fieldPhone.value = contact.phone;
  fieldEmail.value = contact.email || "";
  formError.hidden = true;
  modalOverlay.hidden = false;
  fieldName.focus();
}

function closeModal() {
  modalOverlay.hidden = true;
  editingId = null;
}

document.getElementById("newContactBtn").addEventListener("click", openAddModal);
document.getElementById("cancelBtn").addEventListener("click", closeModal);
modalOverlay.addEventListener("click", (e) => { if (e.target === modalOverlay) closeModal(); });

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  formError.hidden = true;

  const payload = {
    name: fieldName.value.trim(),
    phone: fieldPhone.value.trim(),
    email: fieldEmail.value.trim(),
  };

  const isEdit = editingId !== null;
  const url = isEdit ? `/api/contacts/${editingId}` : "/api/contacts";
  const method = isEdit ? "PUT" : "POST";

  try {
    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();

    if (!res.ok) {
      formError.textContent = data.error || "Something went wrong.";
      formError.hidden = false;
      return;
    }

    closeModal();
    showStatus(isEdit ? "Contact updated." : "Contact added.");
    fetchContacts(searchInput.value.trim());
  } catch (err) {
    formError.textContent = "Could not reach the server. Please try again.";
    formError.hidden = false;
  }
});

// ---------------------------------------------------------------------
// Delete confirmation
// ---------------------------------------------------------------------
function openConfirmDelete(contact) {
  pendingDeleteId = contact.id;
  confirmText.textContent = `"${contact.name}" will be permanently removed from your contact book.`;
  confirmOverlay.hidden = false;
}

function closeConfirm() {
  confirmOverlay.hidden = true;
  pendingDeleteId = null;
}

document.getElementById("confirmCancelBtn").addEventListener("click", closeConfirm);
confirmOverlay.addEventListener("click", (e) => { if (e.target === confirmOverlay) closeConfirm(); });

document.getElementById("confirmDeleteBtn").addEventListener("click", async () => {
  if (!pendingDeleteId) return;
  const res = await fetch(`/api/contacts/${pendingDeleteId}`, { method: "DELETE" });
  closeConfirm();
  if (res.ok) {
    showStatus("Contact removed.");
    fetchContacts(searchInput.value.trim());
  }
});

// ---------------------------------------------------------------------
// Search (debounced)
// ---------------------------------------------------------------------
searchInput.addEventListener("input", () => {
  clearTimeout(searchDebounce);
  searchDebounce = setTimeout(() => {
    fetchContacts(searchInput.value.trim());
  }, 200);
});

// Escape key closes any open overlay
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    if (!modalOverlay.hidden) closeModal();
    if (!confirmOverlay.hidden) closeConfirm();
  }
});

// ---------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------
fetchContacts();
