import reflex as rx
import httpx

API_URL = "http://127.0.0.1:5001/api"


# ---------------------------------------------------------------------------
# STATE
# ---------------------------------------------------------------------------

class State(rx.State):
    """État global de l'application."""

    produits: list[dict] = []
    clients: list[dict] = []
    commandes: list[dict] = []

    nom_produit: str = ""
    description_produit: str = ""
    prix_produit: str = ""
    stock_produit: str = ""

    nom_client: str = ""
    email_client: str = ""
    telephone_client: str = ""

    client_id_commande: str = ""
    produit_id_commande: str = ""
    quantite_commande: str = ""

    # Édition Produit
    edit_produit_id: int = 0
    edit_nom_produit: str = ""
    edit_description_produit: str = ""
    edit_prix_produit: str = ""
    edit_stock_produit: str = ""
    show_edit_produit: bool = False

    # Édition Client
    edit_client_id: int = 0
    edit_nom_client: str = ""
    edit_email_client: str = ""
    edit_telephone_client: str = ""
    show_edit_client: bool = False

    # Édition Commande
    edit_commande_id: int = 0
    edit_quantite_commande: str = ""
    show_edit_commande: bool = False

    # Confirmations
    show_confirm_delete_produit: bool = False
    confirm_delete_produit_id: int = 0
    show_confirm_delete_client: bool = False
    confirm_delete_client_id: int = 0
    show_confirm_delete_commande: bool = False
    confirm_delete_commande_id: int = 0
    show_confirm_add_produit: bool = False
    show_confirm_add_client: bool = False
    show_confirm_add_commande: bool = False
    show_confirm_save_produit: bool = False
    show_confirm_save_client: bool = False
    show_confirm_save_commande: bool = False

    # ---------------- CONFIRMATIONS PRODUITS ----------------

    def ask_add_produit(self):
        if not self.nom_produit or not self.prix_produit:
            return rx.toast.error("Veuillez renseigner au moins le nom et le prix.")
        self.show_confirm_add_produit = True

    def cancel_add_produit(self):
        self.show_confirm_add_produit = False

    def ask_delete_produit(self, produit_id: int):
        self.confirm_delete_produit_id = produit_id
        self.show_confirm_delete_produit = True

    def cancel_delete_produit(self):
        self.show_confirm_delete_produit = False

    def ask_save_produit(self):
        self.show_confirm_save_produit = True

    def cancel_save_produit(self):
        self.show_confirm_save_produit = False

    # ---------------- CONFIRMATIONS CLIENTS ----------------

    def ask_add_client(self):
        if not self.nom_client:
            return rx.toast.error("Veuillez renseigner au moins le nom.")
        self.show_confirm_add_client = True

    def cancel_add_client(self):
        self.show_confirm_add_client = False

    def ask_delete_client(self, client_id: int):
        self.confirm_delete_client_id = client_id
        self.show_confirm_delete_client = True

    def cancel_delete_client(self):
        self.show_confirm_delete_client = False

    def ask_save_client(self):
        self.show_confirm_save_client = True

    def cancel_save_client(self):
        self.show_confirm_save_client = False

    # ---------------- CONFIRMATIONS COMMANDES ----------------

    def ask_add_commande(self):
        if not self.client_id_commande or not self.produit_id_commande:
            return rx.toast.error("Veuillez renseigner le client et le produit.")
        self.show_confirm_add_commande = True

    def cancel_add_commande(self):
        self.show_confirm_add_commande = False

    def ask_delete_commande(self, commande_id: int):
        self.confirm_delete_commande_id = commande_id
        self.show_confirm_delete_commande = True

    def cancel_delete_commande(self):
        self.show_confirm_delete_commande = False

    def ask_save_commande(self):
        self.show_confirm_save_commande = True

    def cancel_save_commande(self):
        self.show_confirm_save_commande = False

    # ---------------- PRODUITS ----------------

    def load_produits(self):
        try:
            res = httpx.get(f"{API_URL}/produits")
            self.produits = res.json()
        except Exception as e:
            print("Erreur load_produits:", e)

    def load_clients(self):
        try:
            res = httpx.get(f"{API_URL}/clients")
            self.clients = res.json()
        except Exception as e:
            print("Erreur load_clients:", e)

    def load_commandes(self):
        try:
            res = httpx.get(f"{API_URL}/commandes")
            self.commandes = res.json()
        except Exception as e:
            print("Erreur load_commandes:", e)

    ventes_par_produit: list[dict] = []
    repartition: list[dict] = []

    def load_ventes_par_produit(self):
        try:
            res = httpx.get(f"{API_URL}/stats/ventes-par-produit")
            data = res.json()
            self.ventes_par_produit = data
            self.repartition = [
                {"name": d["produit"], "value": d["total"]}
                for d in data
            ]
        except Exception as e:
            print("Erreur load_ventes_par_produit:", e)

    def load_all(self):
        self.load_produits()
        self.load_clients()
        self.load_commandes()
        self.load_ventes_par_produit()

    # ---------------- SETTERS EXPLICITES ----------------

    def set_nom_produit(self, value: str):
        self.nom_produit = value

    def set_description_produit(self, value: str):
        self.description_produit = value

    def set_prix_produit(self, value: str):
        self.prix_produit = value

    def set_stock_produit(self, value: str):
        self.stock_produit = value

    def set_nom_client(self, value: str):
        self.nom_client = value

    def set_email_client(self, value: str):
        self.email_client = value

    def set_telephone_client(self, value: str):
        self.telephone_client = value

    def set_client_id_commande(self, value: str):
        self.client_id_commande = value

    def set_produit_id_commande(self, value: str):
        self.produit_id_commande = value

    def set_quantite_commande(self, value: str):
        self.quantite_commande = value

    def set_edit_nom_produit(self, value: str):
        self.edit_nom_produit = value

    def set_edit_description_produit(self, value: str):
        self.edit_description_produit = value

    def set_edit_prix_produit(self, value: str):
        self.edit_prix_produit = value

    def set_edit_stock_produit(self, value: str):
        self.edit_stock_produit = value

    def set_edit_nom_client(self, value: str):
        self.edit_nom_client = value

    def set_edit_email_client(self, value: str):
        self.edit_email_client = value

    def set_edit_telephone_client(self, value: str):
        self.edit_telephone_client = value

    def set_edit_quantite_commande(self, value: str):
        self.edit_quantite_commande = value

    # ---------------- PRODUITS ----------------

    def add_produit(self):
        self.show_confirm_add_produit = False
        try:
            httpx.post(f"{API_URL}/produits", json={
                "nom": self.nom_produit,
                "description": self.description_produit,
                "prix": float(self.prix_produit),
                "stock": int(self.stock_produit) if self.stock_produit else 0,
            })
            self.nom_produit = ""
            self.description_produit = ""
            self.prix_produit = ""
            self.stock_produit = ""
            self.load_produits()
            return rx.toast.success("Produit ajouté avec succès.")
        except Exception as e:
            print("Erreur add_produit:", e)
            return rx.toast.error("Erreur lors de l'ajout du produit.")

    def delete_produit(self):
        self.show_confirm_delete_produit = False
        try:
            httpx.delete(f"{API_URL}/produits/{self.confirm_delete_produit_id}")
            self.load_produits()
            return rx.toast.success("Produit supprimé.")
        except Exception as e:
            print("Erreur delete_produit:", e)
            return rx.toast.error("Erreur lors de la suppression.")

    def open_edit_produit(self, produit: dict):
        self.edit_produit_id = produit["id"]
        self.edit_nom_produit = produit["nom"]
        self.edit_description_produit = produit["description"] or ""
        self.edit_prix_produit = str(produit["prix"])
        self.edit_stock_produit = str(produit["stock"])
        self.show_edit_produit = True

    def close_edit_produit(self):
        self.show_edit_produit = False

    def save_edit_produit(self):
        self.show_confirm_save_produit = False
        try:
            httpx.put(f"{API_URL}/produits/{self.edit_produit_id}", json={
                "nom": self.edit_nom_produit,
                "description": self.edit_description_produit,
                "prix": float(self.edit_prix_produit),
                "stock": int(self.edit_stock_produit) if self.edit_stock_produit else 0,
            })
            self.show_edit_produit = False
            self.load_produits()
            return rx.toast.success("Produit modifié avec succès.")
        except Exception as e:
            print("Erreur save_edit_produit:", e)
            return rx.toast.error("Erreur lors de la modification.")

    # ---------------- CLIENTS ----------------

    def add_client(self):
        self.show_confirm_add_client = False
        try:
            httpx.post(f"{API_URL}/clients", json={
                "nom": self.nom_client,
                "email": self.email_client,
                "telephone": self.telephone_client,
            })
            self.nom_client = ""
            self.email_client = ""
            self.telephone_client = ""
            self.load_clients()
            return rx.toast.success("Client ajouté avec succès.")
        except Exception as e:
            print("Erreur add_client:", e)
            return rx.toast.error("Erreur lors de l'ajout du client.")

    def delete_client(self):
        self.show_confirm_delete_client = False
        try:
            httpx.delete(f"{API_URL}/clients/{self.confirm_delete_client_id}")
            self.load_clients()
            return rx.toast.success("Client supprimé.")
        except Exception as e:
            print("Erreur delete_client:", e)
            return rx.toast.error("Erreur lors de la suppression.")

    def open_edit_client(self, client: dict):
        self.edit_client_id = client["id"]
        self.edit_nom_client = client["nom"]
        self.edit_email_client = client["email"] or ""
        self.edit_telephone_client = client["telephone"] or ""
        self.show_edit_client = True

    def close_edit_client(self):
        self.show_edit_client = False

    def save_edit_client(self):
        self.show_confirm_save_client = False
        try:
            httpx.put(f"{API_URL}/clients/{self.edit_client_id}", json={
                "nom": self.edit_nom_client,
                "email": self.edit_email_client,
                "telephone": self.edit_telephone_client,
            })
            self.show_edit_client = False
            self.load_clients()
            return rx.toast.success("Client modifié avec succès.")
        except Exception as e:
            print("Erreur save_edit_client:", e)
            return rx.toast.error("Erreur lors de la modification.")

    # ---------------- COMMANDES ----------------

    def add_commande(self):
        self.show_confirm_add_commande = False
        try:
            res = httpx.post(f"{API_URL}/commandes", json={
                "client_id": int(self.client_id_commande),
                "produit_id": int(self.produit_id_commande),
                "quantite": int(self.quantite_commande) if self.quantite_commande else 1,
            })
            if res.status_code == 201:
                self.client_id_commande = ""
                self.produit_id_commande = ""
                self.quantite_commande = ""
                self.load_commandes()
                self.load_produits()
                return rx.toast.success("Commande ajoutée avec succès.")
            else:
                return rx.toast.error(res.json().get("error", "Erreur lors de l'ajout."))
        except Exception as e:
            print("Erreur add_commande:", e)
            return rx.toast.error("Erreur lors de l'ajout de la commande.")

    def delete_commande(self):
        self.show_confirm_delete_commande = False
        try:
            httpx.delete(f"{API_URL}/commandes/{self.confirm_delete_commande_id}")
            self.load_commandes()
            self.load_produits()
            return rx.toast.success("Commande supprimée.")
        except Exception as e:
            print("Erreur delete_commande:", e)
            return rx.toast.error("Erreur lors de la suppression.")

    def open_edit_commande(self, commande: dict):
        self.edit_commande_id = commande["id"]
        self.edit_quantite_commande = str(commande["quantite"])
        self.show_edit_commande = True

    def close_edit_commande(self):
        self.show_edit_commande = False

    def save_edit_commande(self):
        self.show_confirm_save_commande = False
        try:
            res = httpx.put(f"{API_URL}/commandes/{self.edit_commande_id}", json={
                "quantite": int(self.edit_quantite_commande) if self.edit_quantite_commande else 1,
            })
            if res.status_code == 200:
                self.show_edit_commande = False
                self.load_commandes()
                self.load_produits()
                return rx.toast.success("Commande modifiée avec succès.")
            else:
                return rx.toast.error(res.json().get("error", "Erreur lors de la modification."))
        except Exception as e:
            print("Erreur save_edit_commande:", e)
            return rx.toast.error("Erreur lors de la modification.")

    # ---------------- STATS ----------------

    # Filtres et tri
    search_produit: str = ""
    sort_produit: str = "nom"
    search_client: str = ""
    sort_client: str = "nom"
    search_commande: str = ""
    sort_commande: str = "date"

    def set_search_produit(self, v: str): self.search_produit = v
    def set_sort_produit(self, v: str): self.sort_produit = v
    def set_search_client(self, v: str): self.search_client = v
    def set_sort_client(self, v: str): self.sort_client = v
    def set_search_commande(self, v: str): self.search_commande = v
    def set_sort_commande(self, v: str): self.sort_commande = v

    @rx.var
    def produits_filtres(self) -> list[dict]:
        items = [p for p in self.produits
                 if self.search_produit.lower() in p.get("nom", "").lower()
                 or self.search_produit.lower() in (p.get("description") or "").lower()]
        if self.sort_produit == "nom":
            items = sorted(items, key=lambda x: x.get("nom", "").lower())
        elif self.sort_produit == "prix_asc":
            items = sorted(items, key=lambda x: x.get("prix", 0))
        elif self.sort_produit == "prix_desc":
            items = sorted(items, key=lambda x: x.get("prix", 0), reverse=True)
        elif self.sort_produit == "stock":
            items = sorted(items, key=lambda x: x.get("stock", 0))
        return items

    @rx.var
    def clients_filtres(self) -> list[dict]:
        items = [c for c in self.clients
                 if self.search_client.lower() in c.get("nom", "").lower()
                 or self.search_client.lower() in (c.get("email") or "").lower()]
        if self.sort_client == "nom":
            items = sorted(items, key=lambda x: x.get("nom", "").lower())
        elif self.sort_client == "email":
            items = sorted(items, key=lambda x: (x.get("email") or "").lower())
        return items

    @rx.var
    def commandes_filtrees(self) -> list[dict]:
        items = [c for c in self.commandes
                 if self.search_commande.lower() in (c.get("client_nom") or "").lower()
                 or self.search_commande.lower() in (c.get("produit_nom") or "").lower()]
        if self.sort_commande == "date":
            items = sorted(items, key=lambda x: x.get("date_commande", ""), reverse=True)
        elif self.sort_commande == "total_desc":
            items = sorted(items, key=lambda x: x.get("total", 0), reverse=True)
        elif self.sort_commande == "total_asc":
            items = sorted(items, key=lambda x: x.get("total", 0))
        elif self.sort_commande == "client":
            items = sorted(items, key=lambda x: (x.get("client_nom") or "").lower())
        return items

    @rx.var
    def nb_produits(self) -> int:
        return len(self.produits)

    @rx.var
    def nb_clients(self) -> int:
        return len(self.clients)

    @rx.var
    def nb_commandes(self) -> int:
        return len(self.commandes)

    @rx.var
    def total_ventes(self) -> float:
        return sum(c.get("total", 0) for c in self.commandes)


# ---------------------------------------------------------------------------
# DESIGN TOKENS
# ---------------------------------------------------------------------------

COLOR_BG = "#F7F7FB"
COLOR_SURFACE = "#FFFFFF"
COLOR_PRIMARY = "#5B5FEF"
COLOR_PRIMARY_SOFT = "#F0F0FD"
COLOR_ACCENT = "#FF6B5B"
COLOR_SUCCESS = "#22C55E"
COLOR_SUCCESS_SOFT = "#EDFAF1"
COLOR_TEXT = "#3D3D52"
COLOR_MUTED = "#A0A0B2"
COLOR_BORDER = "#F0F0F4"

GRADIENT_PRIMARY = "linear-gradient(135deg, #7F77DD 0%, #A78BFA 100%)"
GRADIENT_ACCENT = "linear-gradient(135deg, #F0997B 0%, #FBBF24 100%)"
GRADIENT_SUCCESS = "linear-gradient(135deg, #97C459 0%, #639922 100%)"
GRADIENT_DANGER = "linear-gradient(135deg, #F09595 0%, #E24B4A 100%)"
GRADIENT_INFO = "linear-gradient(135deg, #85B7EB 0%, #378ADD 100%)"
CARD_SHADOW = "0 4px 16px rgba(127, 119, 221, 0.12)"

FONT_DISPLAY = "Outfit, sans-serif"
FONT_BODY = "Inter, sans-serif"

GLOBAL_CSS = """
input::placeholder, textarea::placeholder {
    color: #9999AD !important;
    opacity: 1 !important;
    font-weight: 400 !important;
}
input, textarea {
    color: #3D3D52 !important;
    font-weight: 500 !important;
}
"""


# ---------------------------------------------------------------------------
# COMPOSANTS UI
# ---------------------------------------------------------------------------

def nav_item(label: str, href: str, icon: str) -> rx.Component:
    is_active = rx.State.router.page.path == href
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(label, font_family=FONT_BODY, font_weight="500", size="3"),
            spacing="3",
            align="center",
            width="100%",
            padding="0.65em 1em",
            border_radius="12px",
            background=rx.cond(is_active, COLOR_PRIMARY_SOFT, "transparent"),
            color=rx.cond(is_active, COLOR_PRIMARY, COLOR_MUTED),
            _hover={
                "background": COLOR_PRIMARY_SOFT,
                "color": COLOR_PRIMARY,
            },
            transition="all 0.15s ease",
        ),
        href=href,
        width="100%",
        text_decoration="none",
    )


def sidebar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.icon("trending-up", size=22, color="white"),
                background=GRADIENT_PRIMARY,
                padding="0.55em",
                border_radius="14px",
                box_shadow="0 4px 12px rgba(127, 119, 221, 0.3)",
            ),
            rx.vstack(
                rx.text("Ventes+", font_family=FONT_DISPLAY, font_weight="700",
                        size="4", color=COLOR_TEXT, line_height="1.1"),
                rx.text("Gestion commerciale", font_family=FONT_BODY,
                        size="1", color=COLOR_MUTED),
                spacing="0",
                align="start",
            ),
            spacing="3",
            align="center",
            padding="0.5em 0.5em 1.5em 0.5em",
        ),
        nav_item("Tableau de bord", "/", "layout-dashboard"),
        nav_item("Produits", "/produits", "package"),
        nav_item("Clients", "/clients", "users"),
        nav_item("Commandes", "/commandes", "shopping-cart"),
        nav_item("Statistiques", "/stats", "bar-chart-2"),
        rx.spacer(),
        rx.box(
            rx.vstack(
                rx.text("Astuce", font_family=FONT_DISPLAY, font_weight="600",
                        size="2", color="white"),
                rx.text(
                    "Les IDs Client et Produit sont visibles dans leurs tableaux respectifs.",
                    font_family=FONT_BODY, size="1", color="rgba(255,255,255,0.95)", line_height="1.5",
                    font_weight="500",
                ),
                spacing="1",
                align="start",
            ),
            background=GRADIENT_ACCENT,
            border_radius="16px",
            padding="1em",
            box_shadow="0 4px 12px rgba(240, 153, 123, 0.3)",
        ),
        spacing="2",
        width="260px",
        min_width="260px",
        height="100vh",
        padding="1.5em 1.25em",
        background=COLOR_SURFACE,
        border_right=f"1px solid {COLOR_BORDER}",
        position="sticky",
        top="0",
    )


def page_shell(*children, title: str, subtitle: str = "") -> rx.Component:
    return rx.hstack(
        rx.html("<style>" + GLOBAL_CSS + "</style>"),
        rx.toast.provider(),
        sidebar(),
        rx.vstack(
            rx.vstack(
                rx.heading(title, font_family=FONT_DISPLAY, size="8",
                           color=COLOR_TEXT, font_weight="700"),
                rx.cond(
                    subtitle != "",
                    rx.text(subtitle, font_family=FONT_BODY, color=COLOR_MUTED, size="3"),
                ),
                spacing="1",
                align="start",
                width="100%",
                padding_bottom="1.5em",
            ),
            *children,
            spacing="4",
            width="100%",
            padding="2.5em 3em",
            on_mount=State.load_all,
        ),
        width="100%",
        min_height="100vh",
        background=COLOR_BG,
        spacing="0",
        font_family=FONT_BODY,
        align="start",
    )


def stat_card(label: str, value, icon: str, gradient: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=22, color="white"),
            background="rgba(255,255,255,0.22)",
            padding="0.75em",
            border_radius="14px",
        ),
        rx.vstack(
            rx.text(label, font_family=FONT_BODY, size="2", color="rgba(255,255,255,0.85)", font_weight="500"),
            rx.text(value, font_family=FONT_DISPLAY, size="6", font_weight="700", color="white"),
            spacing="0",
            align="start",
        ),
        spacing="3",
        align="center",
        background=gradient,
        border_radius="18px",
        padding="1.25em 1.5em",
        width="100%",
        box_shadow=CARD_SHADOW,
    )


def form_card(*children, title: str) -> rx.Component:
    return rx.vstack(
        rx.text(title, font_family=FONT_DISPLAY, size="4", font_weight="600", color=COLOR_TEXT),
        rx.hstack(*children, spacing="3", width="100%", flex_wrap="wrap"),
        spacing="3",
        background=COLOR_SURFACE,
        border_radius="20px",
        padding="1.5em",
        width="100%",
        align="start",
        box_shadow=CARD_SHADOW,
    )


def styled_input(**kwargs) -> rx.Component:
    return rx.input(
        border=f"1.5px solid {COLOR_BORDER}",
        border_radius="12px",
        padding="0.75em 1em",
        font_family=FONT_BODY,
        font_size="0.95em",
        font_weight="500",
        background=COLOR_BG,
        color=COLOR_TEXT,
        height="2.75em",
        _placeholder={"color": "#9999AD", "opacity": "1", "font_weight": "400"},
        _focus={"border_color": COLOR_PRIMARY, "outline": "none", "background": COLOR_SURFACE},
        **kwargs,
    )


def primary_button(label: str, **kwargs) -> rx.Component:
    return rx.button(
        rx.hstack(rx.icon("plus", size=16), rx.text(label), spacing="2", align="center"),
        background=GRADIENT_PRIMARY,
        color="white",
        border_radius="14px",
        padding="0.75em 1.5em",
        height="2.75em",
        font_family=FONT_BODY,
        font_weight="600",
        cursor="pointer",
        border="none",
        box_shadow="0 4px 12px rgba(127, 119, 221, 0.3)",
        _hover={"transform": "translateY(-1px)", "box_shadow": "0 6px 16px rgba(127, 119, 221, 0.4)"},
        transition="all 0.15s ease",
        **kwargs,
    )


def delete_button(**kwargs) -> rx.Component:
    return rx.button(
        rx.icon("trash-2", size=16),
        background=COLOR_BG,
        color=COLOR_ACCENT,
        border="none",
        border_radius="12px",
        padding="0.5em",
        cursor="pointer",
        _hover={"background": GRADIENT_DANGER, "color": "white"},
        transition="all 0.15s ease",
        **kwargs,
    )


def edit_button(**kwargs) -> rx.Component:
    return rx.button(
        rx.icon("pencil", size=16),
        background=COLOR_BG,
        color=COLOR_PRIMARY,
        border="none",
        border_radius="12px",
        padding="0.5em",
        cursor="pointer",
        _hover={"background": GRADIENT_PRIMARY, "color": "white"},
        transition="all 0.15s ease",
        **kwargs,
    )


def actions_cell(edit_kwargs: dict, delete_kwargs: dict) -> rx.Component:
    return rx.table.cell(
        rx.hstack(
            edit_button(**edit_kwargs),
            delete_button(**delete_kwargs),
            spacing="2",
        )
    )


def edit_modal(is_open, on_close, title: str, *fields, on_save) -> rx.Component:
    return rx.cond(
        is_open,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text(title, font_family=FONT_DISPLAY, size="5",
                                font_weight="700", color=COLOR_TEXT),
                        rx.spacer(),
                        rx.button(
                            rx.icon("x", size=18),
                            on_click=on_close,
                            background="transparent",
                            border="none",
                            color=COLOR_MUTED,
                            cursor="pointer",
                            padding="0.25em",
                        ),
                        width="100%",
                        align="center",
                    ),
                    rx.vstack(*fields, spacing="3", width="100%"),
                    rx.hstack(
                        rx.button(
                            "Annuler",
                            on_click=on_close,
                            background=COLOR_BG,
                            color=COLOR_TEXT,
                            border="none",
                            border_radius="12px",
                            padding="0.7em 1.4em",
                            font_family=FONT_BODY,
                            font_weight="600",
                            cursor="pointer",
                        ),
                        rx.button(
                            rx.hstack(rx.icon("check", size=16), rx.text("Enregistrer"),
                                      spacing="2", align="center"),
                            on_click=on_save,
                            background=GRADIENT_PRIMARY,
                            color="white",
                            border="none",
                            border_radius="12px",
                            padding="0.7em 1.4em",
                            font_family=FONT_BODY,
                            font_weight="600",
                            cursor="pointer",
                            box_shadow="0 4px 12px rgba(127, 119, 221, 0.3)",
                        ),
                        spacing="3",
                        justify="end",
                        width="100%",
                        margin_top="0.5em",
                    ),
                    spacing="4",
                    width="100%",
                ),
                background=COLOR_SURFACE,
                border_radius="20px",
                padding="2em",
                width="420px",
                box_shadow="0 12px 40px rgba(60, 50, 130, 0.25)",
            ),
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background="rgba(40, 35, 80, 0.35)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="1000",
        ),
    )


def stock_badge(stock) -> rx.Component:
    stock_int = stock.to(int)
    return rx.cond(
        stock_int > 5,
        rx.box(
            rx.text(stock, color="white", font_size="0.85em", font_weight="600",
                    font_family=FONT_BODY),
            background=GRADIENT_SUCCESS,
            padding="0.2em 0.85em",
            border_radius="999px",
            display="inline-block",
        ),
        rx.box(
            rx.text(stock, color="white", font_size="0.85em", font_weight="600",
                    font_family=FONT_BODY),
            background=GRADIENT_DANGER,
            padding="0.2em 0.85em",
            border_radius="999px",
            display="inline-block",
        ),
    )


def data_table(headers: list[str], rows: rx.Component) -> rx.Component:
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    *[
                        rx.table.column_header_cell(
                            h, font_family=FONT_BODY, color=COLOR_MUTED,
                            font_weight="600", font_size="0.85em",
                            text_transform="uppercase", letter_spacing="0.05em",
                        )
                        for h in headers
                    ]
                )
            ),
            rx.table.body(rows),
            width="100%",
            variant="surface",
        ),
        background=COLOR_SURFACE,
        border_radius="20px",
        overflow="hidden",
        width="100%",
        box_shadow=CARD_SHADOW,
    )


# ---------------------------------------------------------------------------
# PAGE TABLEAU DE BORD
# ---------------------------------------------------------------------------

def index() -> rx.Component:
    return page_shell(
        rx.hstack(
            stat_card("Produits", State.nb_produits, "package", GRADIENT_PRIMARY),
            stat_card("Clients", State.nb_clients, "users", GRADIENT_ACCENT),
            stat_card("Commandes", State.nb_commandes, "shopping-cart", GRADIENT_SUCCESS),
            stat_card("Total des ventes", State.total_ventes, "wallet", GRADIENT_INFO),
            spacing="4",
            width="100%",
        ),
        rx.box(
            rx.vstack(
                rx.text("Bienvenue 👋", font_family=FONT_DISPLAY, size="5",
                        font_weight="700", color="white"),
                rx.text(
                    "Gérez vos produits, vos clients et vos commandes depuis ce tableau de bord. "
                    "Utilisez le menu latéral pour naviguer entre les sections.",
                    font_family=FONT_BODY, color="rgba(255,255,255,0.85)", size="3", line_height="1.6",
                ),
                spacing="2",
                align="start",
            ),
            background=GRADIENT_PRIMARY,
            border_radius="20px",
            padding="2em",
            width="100%",
            margin_top="0.5em",
            box_shadow=CARD_SHADOW,
        ),
        title="Tableau de bord",
        subtitle="Vue d'ensemble de votre activité commerciale",
    )


# ---------------------------------------------------------------------------
# PAGE PRODUITS
# ---------------------------------------------------------------------------

def filter_bar(search_value, on_search, sort_value, on_sort, sort_options: list) -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.icon("search", size=16, color=COLOR_MUTED),
            rx.input(
                placeholder="Rechercher...",
                value=search_value,
                on_change=on_search,
                border="none",
                background="transparent",
                font_family=FONT_BODY,
                color=COLOR_TEXT,
                _placeholder={"color": COLOR_MUTED},
                _focus={"outline": "none"},
                width="200px",
            ),
            background=COLOR_SURFACE,
            border=f"1.5px solid {COLOR_BORDER}",
            border_radius="12px",
            padding="0.5em 1em",
            align="center",
            spacing="2",
            box_shadow=CARD_SHADOW,
        ),
        rx.select(
            sort_options,
            value=sort_value,
            on_change=on_sort,
            background=COLOR_SURFACE,
            border=f"1.5px solid {COLOR_BORDER}",
            border_radius="12px",
            font_family=FONT_BODY,
            color=COLOR_TEXT,
            box_shadow=CARD_SHADOW,
        ),
        spacing="3",
        width="100%",
        justify="end",
    )


def confirm_dialog(is_open, title: str, message: str, on_confirm, on_cancel, confirm_label: str = "Confirmer", confirm_color: str = None) -> rx.Component:
    btn_bg = confirm_color or GRADIENT_PRIMARY
    icon_bg = "#FCEBEB" if confirm_color == GRADIENT_DANGER else COLOR_PRIMARY_SOFT
    icon_color = "#A32D2D" if confirm_color == GRADIENT_DANGER else COLOR_PRIMARY
    icon_name = "trash-2" if confirm_color == GRADIENT_DANGER else "circle-check"
    return rx.cond(
        is_open,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon(icon_name, size=20, color=icon_color),
                            background=icon_bg,
                            width="40px",
                            height="40px",
                            border_radius="999px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            flex_shrink="0",
                        ),
                        rx.text(title, font_family=FONT_DISPLAY, size="4",
                                font_weight="700", color=COLOR_TEXT),
                        spacing="3",
                        align="center",
                    ),
                    rx.text(message, font_family=FONT_BODY, color=COLOR_MUTED,
                            size="2", line_height="1.6"),
                    rx.hstack(
                        rx.button(
                            "Annuler",
                            on_click=on_cancel,
                            background=COLOR_BG,
                            color=COLOR_TEXT,
                            border=f"1px solid {COLOR_BORDER}",
                            border_radius="10px",
                            padding="0.6em 1.3em",
                            font_family=FONT_BODY,
                            font_weight="600",
                            font_size="0.9em",
                            cursor="pointer",
                            flex="1",
                        ),
                        rx.button(
                            confirm_label,
                            on_click=on_confirm,
                            background=btn_bg,
                            color="white",
                            border="none",
                            border_radius="10px",
                            padding="0.6em 1.3em",
                            font_family=FONT_BODY,
                            font_weight="600",
                            font_size="0.9em",
                            cursor="pointer",
                            flex="1",
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                background=COLOR_SURFACE,
                border_radius="16px",
                padding="1.75em",
                width="380px",
                border=f"1px solid {COLOR_BORDER}",
                box_shadow="0 8px 32px rgba(60,50,130,0.18)",
            ),
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background="rgba(40,35,80,0.3)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="1001",
        ),
    )



    return rx.hstack(
        rx.hstack(
            rx.icon("search", size=16, color=COLOR_MUTED),
            rx.input(
                placeholder="Rechercher...",
                value=search_value,
                on_change=on_search,
                border="none",
                background="transparent",
                font_family=FONT_BODY,
                color=COLOR_TEXT,
                _placeholder={"color": COLOR_MUTED},
                _focus={"outline": "none"},
                width="200px",
            ),
            background=COLOR_SURFACE,
            border=f"1.5px solid {COLOR_BORDER}",
            border_radius="12px",
            padding="0.5em 1em",
            align="center",
            spacing="2",
            box_shadow=CARD_SHADOW,
        ),
        rx.select(
            sort_options,
            value=sort_value,
            on_change=on_sort,
            background=COLOR_SURFACE,
            border=f"1.5px solid {COLOR_BORDER}",
            border_radius="12px",
            font_family=FONT_BODY,
            color=COLOR_TEXT,
            box_shadow=CARD_SHADOW,
        ),
        spacing="3",
        width="100%",
        justify="end",
    )


def produit_card(produit: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(width="6px", background=COLOR_PRIMARY, flex_shrink="0", align_self="stretch", border_radius="0"),
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.icon("package", size=20, color=COLOR_PRIMARY),
                        background=COLOR_PRIMARY_SOFT,
                        width="40px",
                        height="40px",
                        border_radius="10px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text(produit["nom"], font_family=FONT_DISPLAY, font_weight="700",
                                size="3", color=COLOR_TEXT),
                        rx.text(produit["description"], font_family=FONT_BODY,
                                color=COLOR_MUTED, size="1", line_height="1.3"),
                        spacing="0",
                        align="start",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                rx.box(height="1px", background=COLOR_BORDER, width="100%"),
                rx.hstack(
                    rx.vstack(
                        rx.text("Prix", font_family=FONT_BODY, size="1", color=COLOR_MUTED),
                        rx.text(produit["prix"], font_family=FONT_DISPLAY,
                                font_weight="700", size="4", color=COLOR_TEXT),
                        spacing="0", align="start",
                    ),
                    rx.vstack(
                        rx.text("Stock", font_family=FONT_BODY, size="1", color=COLOR_MUTED),
                        stock_badge(produit["stock"]),
                        spacing="1", align="start",
                    ),
                    rx.spacer(),
                    rx.box(
                        rx.text(f"ID #{produit['id']}", font_family=FONT_BODY, size="1",
                                color=COLOR_PRIMARY, font_weight="600"),
                        background=COLOR_PRIMARY_SOFT,
                        padding="0.15em 0.65em",
                        border_radius="999px",
                    ),
                    rx.hstack(
                        edit_button(on_click=lambda: State.open_edit_produit(produit)),
                        delete_button(on_click=lambda: State.ask_delete_produit(produit["id"])),
                        spacing="1",
                    ),
                    width="100%",
                    align="center",
                ),
                spacing="3",
                padding="1rem",
                width="100%",
                align="start",
            ),
            spacing="0",
            width="100%",
        ),
        background=COLOR_SURFACE,
        border=f"0.5px solid {COLOR_BORDER}",
        border_radius="16px",
        overflow="hidden",
        width="320px",
        box_shadow=CARD_SHADOW,
        _hover={"box_shadow": "0 8px 24px rgba(127,119,221,0.18)", "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
    )


def produits_page() -> rx.Component:
    return page_shell(
        filter_bar(
            State.search_produit, State.set_search_produit,
            State.sort_produit, State.set_sort_produit,
            ["nom", "prix_asc", "prix_desc", "stock"],
        ),
        form_card(
            styled_input(placeholder="Nom du produit", value=State.nom_produit,
                         on_change=State.set_nom_produit, width="200px"),
            styled_input(placeholder="Description", value=State.description_produit,
                         on_change=State.set_description_produit, width="220px"),
            styled_input(placeholder="Prix", value=State.prix_produit,
                         on_change=State.set_prix_produit, type="number", width="120px"),
            styled_input(placeholder="Stock", value=State.stock_produit,
                         on_change=State.set_stock_produit, type="number", width="120px"),
            primary_button("Ajouter", on_click=State.ask_add_produit),
            title="Ajouter un produit",
        ),
        rx.flex(
            rx.foreach(State.produits_filtres, produit_card),
            wrap="wrap",
            gap="1.25em",
            width="100%",
        ),
        confirm_dialog(
            State.show_confirm_add_produit,
            "Confirmer l'ajout",
            "Voulez-vous ajouter ce produit ?",
            State.add_produit,
            State.cancel_add_produit,
            confirm_label="Oui, ajouter",
        ),
        confirm_dialog(
            State.show_confirm_delete_produit,
            "Confirmer la suppression",
            "Voulez-vous vraiment supprimer ce produit ? Cette action est irréversible.",
            State.delete_produit,
            State.cancel_delete_produit,
            confirm_label="Oui, supprimer",
            confirm_color=GRADIENT_DANGER,
        ),
        edit_modal(
            State.show_edit_produit, State.close_edit_produit, "Modifier le produit",
            styled_input(placeholder="Nom du produit", value=State.edit_nom_produit,
                          on_change=State.set_edit_nom_produit, width="100%"),
            styled_input(placeholder="Description", value=State.edit_description_produit,
                          on_change=State.set_edit_description_produit, width="100%"),
            styled_input(placeholder="Prix", value=State.edit_prix_produit,
                          on_change=State.set_edit_prix_produit, type="number", width="100%"),
            styled_input(placeholder="Stock", value=State.edit_stock_produit,
                          on_change=State.set_edit_stock_produit, type="number", width="100%"),
            on_save=State.ask_save_produit,
        ),
        confirm_dialog(
            State.show_confirm_save_produit,
            "Confirmer la modification",
            "Voulez-vous enregistrer les modifications de ce produit ?",
            State.save_edit_produit,
            State.cancel_save_produit,
            confirm_label="Oui, modifier",
        ),
        title="Produits",
        subtitle="Gérez votre catalogue et suivez les niveaux de stock",
    )


# ---------------------------------------------------------------------------
# PAGE CLIENTS
# ---------------------------------------------------------------------------

def client_card(client: dict) -> rx.Component:
    initiale = client["nom"].to(str)[0]
    return rx.box(
        rx.hstack(
            rx.box(width="6px", background=GRADIENT_ACCENT, flex_shrink="0", align_self="stretch", border_radius="0"),
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text(initiale, color="white", font_family=FONT_DISPLAY,
                                font_weight="700", size="4"),
                        background=GRADIENT_ACCENT,
                        width="40px",
                        height="40px",
                        border_radius="10px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        flex_shrink="0",
                    ),
                    rx.vstack(
                        rx.text(client["nom"], font_family=FONT_DISPLAY, font_weight="700",
                                size="3", color=COLOR_TEXT),
                        rx.box(
                            rx.text(f"ID #{client['id']}", font_family=FONT_BODY, size="1",
                                    color=COLOR_PRIMARY, font_weight="600"),
                            background=COLOR_PRIMARY_SOFT,
                            padding="0.15em 0.65em",
                            border_radius="999px",
                        ),
                        spacing="1",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        edit_button(on_click=lambda: State.open_edit_client(client)),
                        delete_button(on_click=lambda: State.ask_delete_client(client["id"])),
                        spacing="1",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                rx.box(height="1px", background=COLOR_BORDER, width="100%"),
                rx.vstack(
                    rx.hstack(
                        rx.icon("mail", size=14, color=COLOR_MUTED),
                        rx.text(client["email"], font_family=FONT_BODY, color=COLOR_MUTED, size="2"),
                        spacing="2", align="center",
                    ),
                    rx.hstack(
                        rx.icon("phone", size=14, color=COLOR_MUTED),
                        rx.text(client["telephone"], font_family=FONT_BODY, color=COLOR_MUTED, size="2"),
                        spacing="2", align="center",
                    ),
                    spacing="2",
                    align="start",
                    width="100%",
                ),
                spacing="3",
                padding="1rem",
                width="100%",
                align="start",
            ),
            spacing="0",
            width="100%",
        ),
        background=COLOR_SURFACE,
        border=f"0.5px solid {COLOR_BORDER}",
        border_radius="16px",
        overflow="hidden",
        width="320px",
        box_shadow=CARD_SHADOW,
        _hover={"box_shadow": "0 8px 24px rgba(240,153,123,0.18)", "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
    )


def clients_page() -> rx.Component:
    return page_shell(
        filter_bar(
            State.search_client, State.set_search_client,
            State.sort_client, State.set_sort_client,
            ["nom", "email"],
        ),
        form_card(
            styled_input(placeholder="Nom", value=State.nom_client,
                         on_change=State.set_nom_client, width="200px"),
            styled_input(placeholder="Email", value=State.email_client,
                         on_change=State.set_email_client, width="220px"),
            styled_input(placeholder="Téléphone", value=State.telephone_client,
                         on_change=State.set_telephone_client, width="180px"),
            primary_button("Ajouter", on_click=State.ask_add_client),
            title="Ajouter un client",
        ),
        rx.flex(
            rx.foreach(State.clients_filtres, client_card),
            wrap="wrap",
            gap="1.25em",
            width="100%",
        ),
        confirm_dialog(
            State.show_confirm_add_client,
            "Confirmer l'ajout",
            "Voulez-vous ajouter ce client ?",
            State.add_client,
            State.cancel_add_client,
            confirm_label="Oui, ajouter",
        ),
        confirm_dialog(
            State.show_confirm_delete_client,
            "Confirmer la suppression",
            "Voulez-vous vraiment supprimer ce client ?",
            State.delete_client,
            State.cancel_delete_client,
            confirm_label="Oui, supprimer",
            confirm_color=GRADIENT_DANGER,
        ),
        edit_modal(
            State.show_edit_client, State.close_edit_client, "Modifier le client",
            styled_input(placeholder="Nom", value=State.edit_nom_client,
                          on_change=State.set_edit_nom_client, width="100%"),
            styled_input(placeholder="Email", value=State.edit_email_client,
                          on_change=State.set_edit_email_client, width="100%"),
            styled_input(placeholder="Téléphone", value=State.edit_telephone_client,
                          on_change=State.set_edit_telephone_client, width="100%"),
            on_save=State.ask_save_client,
        ),
        confirm_dialog(
            State.show_confirm_save_client,
            "Confirmer la modification",
            "Voulez-vous enregistrer les modifications de ce client ?",
            State.save_edit_client,
            State.cancel_save_client,
            confirm_label="Oui, modifier",
        ),
        title="Clients",
        subtitle="Votre carnet d'adresses commercial",
    )


# ---------------------------------------------------------------------------
# PAGE COMMANDES
# ---------------------------------------------------------------------------

def commande_card(commande: dict) -> rx.Component:
    return rx.box(
        rx.box(
            width="6px",
            background=GRADIENT_INFO,
            position="absolute",
            left="0",
            top="0",
            bottom="0",
            border_radius="16px 0 0 16px",
        ),
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon("shopping-cart", size=20, color="#378ADD"),
                    background="#E6F1FB",
                    width="40px",
                    height="40px",
                    border_radius="10px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(commande["client_nom"], font_family=FONT_DISPLAY,
                            font_weight="700", size="3", color=COLOR_TEXT),
                    rx.text(commande["produit_nom"], font_family=FONT_BODY,
                            color=COLOR_MUTED, size="1"),
                    spacing="0",
                    align="start",
                ),
                rx.spacer(),
                rx.box(
                    rx.text(commande["total"], color="white", font_size="0.8em",
                            font_weight="700", font_family=FONT_BODY),
                    background=GRADIENT_PRIMARY,
                    padding="0.2em 0.85em",
                    border_radius="999px",
                    flex_shrink="0",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            rx.box(height="1px", background=COLOR_BORDER, width="100%"),
            rx.vstack(
                rx.hstack(
                    rx.icon("layers", size=13, color=COLOR_MUTED),
                    rx.text("Quantité : ", font_family=FONT_BODY, color=COLOR_MUTED, size="1"),
                    rx.text(commande["quantite"], font_family=FONT_BODY,
                            color=COLOR_TEXT, font_weight="600", size="1"),
                    spacing="1", align="center",
                ),
                rx.hstack(
                    rx.icon("calendar", size=13, color=COLOR_MUTED),
                    rx.text(commande["date_commande"], font_family=FONT_BODY,
                            color=COLOR_MUTED, size="1"),
                    spacing="1", align="center",
                    overflow="hidden",
                ),
                spacing="1",
                align="start",
                width="100%",
            ),
            rx.hstack(
                rx.spacer(),
                edit_button(on_click=lambda: State.open_edit_commande(commande)),
                delete_button(on_click=lambda: State.ask_delete_commande(commande["id"])),
                spacing="2",
                width="100%",
                align="center",
            ),
            spacing="3",
            padding="1rem",
            padding_left="1.5rem",
            width="100%",
            align="start",
        ),
        background=COLOR_SURFACE,
        border=f"0.5px solid {COLOR_BORDER}",
        border_radius="16px",
        position="relative",
        width="360px",
        box_shadow=CARD_SHADOW,
        _hover={"box_shadow": "0 8px 24px rgba(133,183,235,0.2)", "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
    )


def commandes_page() -> rx.Component:
    return page_shell(
        filter_bar(
            State.search_commande, State.set_search_commande,
            State.sort_commande, State.set_sort_commande,
            ["date", "total_desc", "total_asc", "client"],
        ),
        form_card(
            styled_input(placeholder="ID Client", value=State.client_id_commande,
                         on_change=State.set_client_id_commande, type="number", width="140px"),
            styled_input(placeholder="ID Produit", value=State.produit_id_commande,
                         on_change=State.set_produit_id_commande, type="number", width="140px"),
            styled_input(placeholder="Quantité", value=State.quantite_commande,
                         on_change=State.set_quantite_commande, type="number", width="140px"),
            primary_button("Ajouter", on_click=State.ask_add_commande),
            title="Nouvelle commande",
        ),
        rx.flex(
            rx.foreach(State.commandes_filtrees, commande_card),
            wrap="wrap",
            gap="1.25em",
            width="100%",
        ),
        confirm_dialog(
            State.show_confirm_add_commande,
            "Confirmer l'ajout",
            "Voulez-vous créer cette commande ?",
            State.add_commande,
            State.cancel_add_commande,
            confirm_label="Oui, créer",
        ),
        confirm_dialog(
            State.show_confirm_delete_commande,
            "Confirmer la suppression",
            "Voulez-vous vraiment supprimer cette commande ?",
            State.delete_commande,
            State.cancel_delete_commande,
            confirm_label="Oui, supprimer",
            confirm_color=GRADIENT_DANGER,
        ),
        edit_modal(
            State.show_edit_commande, State.close_edit_commande, "Modifier la quantité",
            styled_input(placeholder="Quantité", value=State.edit_quantite_commande,
                          on_change=State.set_edit_quantite_commande, type="number", width="100%"),
            on_save=State.ask_save_commande,
        ),
        confirm_dialog(
            State.show_confirm_save_commande,
            "Confirmer la modification",
            "Voulez-vous modifier la quantité de cette commande ?",
            State.save_edit_commande,
            State.cancel_save_commande,
            confirm_label="Oui, modifier",
        ),
        title="Commandes",
        subtitle="Historique et suivi des ventes",
    )


# ---------------------------------------------------------------------------
# PAGE STATISTIQUES
# ---------------------------------------------------------------------------

PIE_COLORS = ["#7F77DD", "#FF6B5B", "#22C55E", "#85B7EB", "#FBBF24", "#A78BFA"]


def stats_page() -> rx.Component:
    return page_shell(
        rx.hstack(
            stat_card("Produits", State.nb_produits, "package", GRADIENT_PRIMARY),
            stat_card("Clients", State.nb_clients, "users", GRADIENT_ACCENT),
            stat_card("Commandes", State.nb_commandes, "shopping-cart", GRADIENT_SUCCESS),
            stat_card("Total des ventes", State.total_ventes, "wallet", GRADIENT_INFO),
            spacing="4",
            width="100%",
        ),
        rx.hstack(
            # Graphique en barres
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("bar-chart-2", size=18, color=COLOR_PRIMARY),
                            background=COLOR_PRIMARY_SOFT,
                            padding="0.5em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("Ventes par produit", font_family=FONT_DISPLAY,
                                    font_weight="700", size="4", color=COLOR_TEXT),
                            rx.text("Total des ventes en Ar par produit",
                                    font_family=FONT_BODY, size="1", color=COLOR_MUTED),
                            spacing="0",
                            align="start",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.recharts.bar_chart(
                        rx.recharts.bar(
                            rx.recharts.cell(fill="#7F77DD"),
                            rx.recharts.cell(fill="#FF6B5B"),
                            rx.recharts.cell(fill="#22C55E"),
                            rx.recharts.cell(fill="#85B7EB"),
                            rx.recharts.cell(fill="#FBBF24"),
                            rx.recharts.cell(fill="#A78BFA"),
                            data_key="total",
                            radius=6,
                        ),
                        rx.recharts.x_axis(
                            data_key="produit",
                            tick={"fill": COLOR_MUTED, "fontSize": 12},
                        ),
                        rx.recharts.y_axis(
                            tick={"fill": COLOR_MUTED, "fontSize": 12},
                        ),
                        rx.recharts.cartesian_grid(
                            stroke_dasharray="4 4",
                            stroke=COLOR_BORDER,
                            vertical=False,
                        ),
                        rx.recharts.graphing_tooltip(
                            content_style={
                                "background": COLOR_SURFACE,
                                "border": f"1px solid {COLOR_BORDER}",
                                "borderRadius": "12px",
                                "fontSize": "13px",
                            }
                        ),
                        data=State.ventes_par_produit,
                        width="100%",
                        height=320,
                        margin={"top": 10, "right": 10, "left": 10, "bottom": 10},
                    ),
                    spacing="4",
                    width="100%",
                    align="start",
                ),
                background=COLOR_SURFACE,
                border_radius="20px",
                padding="1.5em",
                flex="1",
                box_shadow=CARD_SHADOW,
            ),
            # Camembert
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("pie-chart", size=18, color=COLOR_ACCENT),
                            background="#FFF1EF",
                            padding="0.5em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("Répartition des ventes", font_family=FONT_DISPLAY,
                                    font_weight="700", size="4", color=COLOR_TEXT),
                            rx.text("Part de chaque produit en %",
                                    font_family=FONT_BODY, size="1", color=COLOR_MUTED),
                            spacing="0",
                            align="start",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.recharts.pie_chart(
                        rx.recharts.pie(
                            rx.recharts.cell(fill="#7F77DD"),
                            rx.recharts.cell(fill="#FF6B5B"),
                            rx.recharts.cell(fill="#22C55E"),
                            rx.recharts.cell(fill="#85B7EB"),
                            rx.recharts.cell(fill="#FBBF24"),
                            rx.recharts.cell(fill="#A78BFA"),
                            data=State.repartition,
                            data_key="value",
                            name_key="name",
                            cx="50%",
                            cy="50%",
                            outer_radius=110,
                            label=True,
                        ),
                        rx.recharts.graphing_tooltip(
                            content_style={
                                "background": COLOR_SURFACE,
                                "border": f"1px solid {COLOR_BORDER}",
                                "borderRadius": "12px",
                                "fontSize": "13px",
                            }
                        ),
                        rx.recharts.legend(),
                        width="100%",
                        height=320,
                    ),
                    spacing="4",
                    width="100%",
                    align="start",
                ),
                background=COLOR_SURFACE,
                border_radius="20px",
                padding="1.5em",
                flex="1",
                box_shadow=CARD_SHADOW,
            ),
            spacing="4",
            width="100%",
            align="start",
        ),
        title="Statistiques",
        subtitle="Analyse de vos performances commerciales",
    )


# ---------------------------------------------------------------------------
# APP
# ---------------------------------------------------------------------------

app = rx.App(
    style={"font_family": FONT_BODY},
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap",
    ],
)
app.add_page(index, route="/")
app.add_page(produits_page, route="/produits")
app.add_page(clients_page, route="/clients")
app.add_page(commandes_page, route="/commandes")
app.add_page(stats_page, route="/stats") 