// ==========================
// SEARCH FILTER (Find Tutors Page)
// ==========================

const searchInput = document.querySelector("input[name='search']");

if (searchInput) {
    searchInput.addEventListener("keyup", function () {

        let filter = searchInput.value.toLowerCase();
        let cards = document.querySelectorAll(".card");

        cards.forEach(card => {

            let text = card.innerText.toLowerCase();

            if (text.includes(filter)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }

        });

    });
}


// ==========================
// BOOK BUTTON FUNCTION
// ==========================

const bookButtons = document.querySelectorAll(".card button");

if (bookButtons.length > 0) {
    bookButtons.forEach(button => {

        button.addEventListener("click", function () {
            alert("Tutor booked successfully!");
        });

    });
}


// ==========================
// APPROVE / REJECT (Admin Panel Safe)
// ==========================

const approveButtons = document.querySelectorAll(".approve-btn");

if (approveButtons.length > 0) {
    approveButtons.forEach(button => {

        button.addEventListener("click", function () {
            alert("Tutor Approved!");
            this.closest(".card, .row, div").remove();
        });

    });
}

const rejectButtons = document.querySelectorAll(".reject-btn");

if (rejectButtons.length > 0) {
    rejectButtons.forEach(button => {

        button.addEventListener("click", function () {
            alert("Tutor Rejected!");
            this.closest(".card, .row, div").remove();
        });

    });
}


// ==========================
// LOGIN VALIDATION (SAFE)
// ==========================

const forms = document.querySelectorAll("form");

if (forms.length > 0) {
    forms.forEach(form => {

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
}