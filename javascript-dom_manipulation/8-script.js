document.addEventListener("DOMContentLoaded", () => { // Define the event listener
	const helloElement = document.getElementById("hello");

	async function fetchAndDisplayTranslation() {
		try {
			const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
			if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
			const translation = await response.text(); // Parse the data
			helloElement.textContent = translation;
		} catch (error) { // Handle the error
			console.error("Fetch error:", error); // Log the error
		}
	}

	fetchAndDisplayTranslation();
});
