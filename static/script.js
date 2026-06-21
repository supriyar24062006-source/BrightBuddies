// ==========================
// SEARCH FILTER (Find Tutors Page)
// ==========================

const searchInput = document.querySelector("input[name='search']");
const cards = document.querySelectorAll(".card");

if (searchInput && cards.length > 0) {

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

        // No results message
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