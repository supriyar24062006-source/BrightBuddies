// ==========================
// SEARCH FILTER (Find Tutors Page)
// ==========================

const searchInput = document.querySelector("input[name='search']");
const cards = document.querySelectorAll(".card");

if (searchInput) {

    searchInput.addEventListener("input", function () {

        let filter = searchInput.value.toLowerCase();
        let found = false;

        cards.forEach(card => {

            let text = card.innerText.toLowerCase();

            if (text.includes(filter)) {
                card.style.display = "block";
                found = true;
            } else {
                card.style.display = "none";
            }

        });

        // show "not found" message
        let msg = document.getElementById("no-results");

        if (!msg) {
            msg = document.createElement("p");
            msg.id = "no-results";
            msg.style.textAlign = "center";
            msg.style.marginTop = "20px";
            msg.style.color = "red";
            document.querySelector(".card-container")?.after(msg);
        }

        msg.innerText = found ? "" : "No tutors available for this subject";

    });

}


// ==========================
// BOOK BUTTON FUNCTION
// ==========================

document.querySelectorAll(".card button").forEach(button => {

    button.addEventListener("click", function () {
        alert("Tutor booked successfully!");
    });

});


// ==========================
// APPROVE / REJECT (ADMIN SAFE)
// ==========================

document.querySelectorAll(".approve-btn").forEach(button => {

    button.addEventListener("click", function () {
        alert("Tutor Approved!");
        this.closest(".card, .row, div")?.remove();
    });

});

document.querySelectorAll(".reject-btn").forEach(button => {

    button.addEventListener("click", function () {
        alert("Tutor Rejected!");
        this.closest(".card, .row, div")?.remove();
    });

});


// ==========================
// LOGIN VALIDATION
// ==========================

document.querySelectorAll("form").forEach(form => {

    form.addEventListener("submit", function (e) {

        let email = form.querySelector("input[type='email']");
        let password = form.querySelector("input[type='password']");

        if (email && password) {

            if (email.value.trim() === "" || password.value.trim() === "") {
                e.preventDefault();
                alert("Please fill all fields.");
            }

        }

    });

});