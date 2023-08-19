var langs =
    [['English', 
    ['en-IN', 'India'],
    ['en-GB', 'United Kingdom'],
    ['en-US', 'United States']],
['Kashmiri',['India']]];

let select_language = document.querySelector('#select_language');
let select_dialect = "en-IN"; 

for (var i = 0; i < langs.length; i++) {
    select_language.options[i] = new Option(langs[i][0], i);
}

  function showFormElements() {
    var dropdown = document.getElementById("select_language");
    var selectedOption = dropdown.options[dropdown.selectedIndex].value;
    // var formElementsContainer = document.getElementById("formElementsContainer");
    if (selectedOption === "option1") {
        document.getElementById("start").style.display = "block";
        document.getElementById("stop").style.display = "block";
        document.getElementById("status").style.display = "block"; 
    //   formElementsContainer.innerHTML = '<label for="myTextBox">Enter Text:</label>  <textarea spellcheck="false" readonly="" disabled="" class="to-text" id="demo" placeholder="Translation"</textarea>';
    } else if (selectedOption === "option2") {
            document.getElementById("start").style.display = "none";
            document.getElementById("stop").style.display = "none";
            document.getElementById("status").style.display = "none";
        // formElementsContainer.innerHTML = '<label for="myInputBox">Enter Input:</label> <input type="text" id="myInputBox" name="myInputBox">';
    }else {
      formElementsContainer.innerHTML = '';
    }
  } 

 
     
  
  
  /* select_language.selectedIndex = 6;
updateCountry();
select_dialect.selectedIndex = 6;

function updateCountry() {
    for (var i = select_dialect.options.length - 1; i >= 0; i--) {
        select_dialect.remove(i);
    }
    var list = langs[select_language.selectedIndex];
    for (var i = 1; i < list.length; i++) {
        select_dialect.options.add(new Option(list[i][1], list[i][0]));
    }
    select_dialect.style.visibility = list[1].length == 1 ? 'hidden' : 'visible';
}  */
// document.getElementById("select_language").addEventListener("change", myFunction);
/* 
  function myFunction() {
    var dropdown = document.getElementById("select_language");
    var selectedOption = dropdown.options[dropdown.selectedIndex].value;
    // if (selectedOption === "option2") {
        if (selectedOption === "Kashmiri") {
        document.getElementById("start").style.display = "none";
        document.getElementById("stop").style.display = "none";
        document.getElementById("status").style.display = "none";
  } else {
    document.getElementById("start").style.display = "block";
    document.getElementById("stop").style.display = "block";
    document.getElementById("status").style.display = "block";   
    }
  } */
  //twoCalls = e => {
    //this.myFunction(e)
   // this.showFormElements()
    // this.myFunction()
 // }



/*   function addTextInput() {
    var dropdown = document.getElementById("select_language");
    var selectedOption = dropdown.options[dropdown.selectedIndex].value;
    var textInputContainer = document.getElementById("textInputContainer");
    if (selectedOption === "option2") {
      textInputContainer.innerHTML = '<label for="myTextInput">Enter Text:</label> <input type="text" id="myTextInput" name="myTextInput">';
    } else {
      textInputContainer.innerHTML = '';
    }
  } */