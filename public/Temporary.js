document.querySelector("#Temp").addEventListener("change", showAdditionalElements);
function showAdditionalElements() {
    var selectedOption = document.getElementById("Temp").value;
    var additionalElementsDiv = document.getElementById("choice");
  
    if (selectedOption === "Temporary") {
      additionalElementsDiv.style.display = "block";
    } else {
      additionalElementsDiv.style.display = "none";
    }
  }