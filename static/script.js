// ==========================
// Tutor Search Function
// ==========================

const searchInput = document.querySelector("input[type='text']");

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
// Book Session Buttons
// ==========================

const bookButtons = document.querySelectorAll("button");

bookButtons.forEach(button => {

    if (
        button.innerText === "Book Now" ||
        button.innerText === "Book Session"
    ) {

        button.addEventListener("click", function () {

            alert("Tutor booked successfully!");

        });

    }

});


// ==========================
// Tutor Approval Section
// ==========================

const approveButtons = document.querySelectorAll(".approve-btn");

approveButtons.forEach(button => {

    button.addEventListener("click", function () {

        alert("Tutor Approved!");

        this.parentElement.parentElement.remove();

    });

});

const rejectButtons = document.querySelectorAll(".reject-btn");

rejectButtons.forEach(button => {

    button.addEventListener("click", function () {

        alert("Tutor Rejected!");

        this.parentElement.parentElement.remove();

    });

});


// ==========================
// Login Validation
// ==========================

const forms = document.querySelectorAll("form");

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