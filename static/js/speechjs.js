if ("webkitSpeechRecognition" in window) {
    // Initialize webkitSpeechRecognition
    let speechRecognition = new webkitSpeechRecognition();
    
    // String for the Final Transcript
    let final_transcript = "";

    // Set the properties for the Speech Recognition object
    speechRecognition.continuous = true;
    speechRecognition.interimResults = true;
    // speechRecognition.lang = document.querySelector("#select_dialect").value;
    // Set the onClick property of the start button
    document.querySelector("#start").onclick = () => {
        // Start the Speech Recognition
        speechRecognition.start();
    };
    // Set the onClick property of the stop button
    document.querySelector("#stop").onclick = () => {
        // Stop the Speech Recognition
        speechRecognition.stop();
        speechRecognition.onresult = (event) => {
            // Create the interim transcript string locally because we don't want it to persist like final transcript
            let interim_transcript = "";
            //var text_kashmiri= document.getElementById("input-text");
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
                type: 'POST',
                data: final_transcript,
                url: 'http://127.0.0.1:5000/index',
                success: function (e) {
                    console.log(e);
                    },
                error: function(error) {
                console.log(error);
            }          
            });
            fetch(`${window.origin}/index`, {
                method: 'GET',
                credentials: "include",
                body: final_transcript,
                cache: "no-cache"
                
              })*/
              /*$.ajax({
                url: '/index',
                type: 'POST',
                data: { 'var1': final_transcript, 'var2': text_kashmiri},
                success: function(response) {
                    console.log("Request succeeded:", response);
                },
                error: function(xhr, status, error) {
                    console.log("Request failed:", error);
                }
                });
                fetch(`${window.origin}/eng`, {
                        method: 'POST',
                        credentials: "include",
                        body: final_transcript,
                        cache: "no-cache"
                        
                      })
                */
                //final_transcript = 'Hello, How are you?'
                if(final_transcript.length !== 0) {
                    console.log(final_transcript.length);
                    console.log("inside IF");                    
                      $(document).ready(function() {
                        $('#demos').click(function() {
                            $.ajax({
                                type: 'POST',
                                url: '/eng',
                                data: {result: final_transcript},
                                success: function(response) {
                                    $('#translate').text(response.result);
                                }
                            });
                        });
                    });
                    }
                
            // Set the Final transcript and Interim transcript.
            document.querySelector("#final").innerHTML = final_transcript;
            document.querySelector("#interim").innerHTML = interim_transcript;
            
        };
    };
    // Callback Function for the onStart Event
    speechRecognition.onstart = () => {
        // Show the Status Element
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

       
    
} else {
    console.log("Speech Recognition Not Available");
}
