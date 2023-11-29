"use strict";
document.addEventListener('DOMContentLoaded', () => {
    const add_contact = document.getElementById("add");
    const delete_contact = document.getElementById("delete");
    const update_contact = document.getElementById("update");
    add_contact.onclick = () => {
        if (confirm("Proceed to Add Contact?")) {
            add_contact.href += "/new_contact";
        }
    };
    delete_contact.onclick = () => {
        if (confirm("Proceed to Delete Contact?")) {
            delete_contact.href += "/delete_contact";
        }
    };
    update_contact.onclick = () => {
        if (confirm("Proceed to Update Contact?")) {
            update_contact.href += "/update";
        }
    };
});
