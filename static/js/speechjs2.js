if ("webkitSpeechRecognition" in window){
  
    let speechRecognition = new webkitSpeechRecognition();

    let final_transcript = "";
    var text_kashmiri= document.getElementById("input-text");
    
    speechRecognition.continuous = true;
    speechRecognition.interimResults = true;
    // speechRecognition.lang = document.querySelector("#select_dialect").value;
    speechRecognition.lang = "en-IN";
   
    speechRecognition.onstart = () => {
   
        document.querySelector("#status").style.display = "block";
    };
    speechRecognition.onerror = () => {
        // Hide the Status Element
        document.querySelector("#status").style.display = "none";
    };
    speechRecognition.onend = () => {
        // Hide the Status Element
        document.querySelector("#status").style.display = "none";
    };
    speechRecognition.onresult = (event) => {
        let interim_transcript = "";

        // Loop through the results from the speech recognition object.
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            // If the result item is Final, add it to Final Transcript, Else add it to Interim transcript
        if (event.results[i].isFinal) {
            final_transcript += event.results[i][0].transcript;
        } else {
            interim_transcript += event.results[i][0].transcript;
        }
    };
        /*$.ajax({
            url: '/index',
            type: "POST",
            data: final_transcript
            
        });*/
        
    $.ajax({
    url: '/index',
    type: 'POST',
    data: { var1: final_transcript, var2: text_kashmiri}
    });
        // Set the Final transcript and Interim transcript.
    document.querySelector("#final").innerHTML = final_transcript;
    document.querySelector("#interim").innerHTML = interim_transcript;
    // };
    
    // Set the onClick property of the start button
    document.querySelector("#start").onclick = () => {
        // Start the Speech Recognition
        speechRecognition.start();
    };
    // Set the onClick property of the stop button
    document.querySelector("#stop").onclick = () => {
        // Stop the Speech Recognition
        speechRecognition.stop();
    }; 
else {
    console.log("Speech Recognition Not Available");
}