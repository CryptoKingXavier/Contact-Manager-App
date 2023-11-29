from contact_app.utils.create_contact import add_contact
from contact_app.utils.delete_contact import delete_contact
from contact_app.utils.update_contact import update_contact
from contact_app.utils.view_contact import show_contacts, show_contact
from flask import Blueprint, render_template, request, url_for, redirect, Response

main: Blueprint = Blueprint("main", __name__)


@main.get("/")
def index() -> str:
    return render_template("index.html")

# View all contacts
@main.get("/contacts")
def contacts() -> str:
    return render_template("view_contacts.html", contacts=show_contacts())

# View a single contact
@main.post("/contact")
def contact() -> str:
    return render_template("view_contact.html", contact=show_contact(request.form['contact_name']))

# Add a new contact
@main.route("/new_contact", methods=['GET', 'POST'])
def new_contact() -> Response:
    if request.method == 'POST':
        add_contact(request.form['contact_name'], request.form['contact_number'])
        return redirect(url_for("main.contacts"))
    return render_template("add_contact.html")

# Delete a contact
@main.route("/delete_contact", methods=['GET', 'POST'])
def remove_contact() -> Response:
    if request.method == 'POST':
        delete_contact(request.form['contact_name'])
        return redirect(url_for("main.contacts"))
    return render_template("delete_contact.html")

# Update a contact
@main.route("/update", methods=['GET', 'POST'])
def update() -> Response:
    if request.method == 'POST':
        update_contact(request.form['contact_name'], request.form['new_name'], request.form['new_number'])
        return redirect(url_for('main.contacts'))
    return render_template("update_contact.html")
