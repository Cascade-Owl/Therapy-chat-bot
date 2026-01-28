const chatBubble = document.getElementById("chatBubble");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");

function appendMessage(sender, text) {
    const chatDiv = document.createElement("div");

    chatDiv.classList.add("message", sender);

    chatDiv.innerText = text;

    chatBubble.appendChild(chatDiv);

    chatDiv.scrollTop = chatDiv.scrollHeight;
}

chatForm.addEventListener("submit", async function (event){
    event.preventDefault();

    const inputText = userInput.value;

    appendMessage("user", inputText);

    if (!(inputText)) return;

    userInput.value = "";

    try{
        const response = await fetch("/botchat", {
            method: "POST",
            headers: {"Content-Type" : "application/json"},
            body: JSON.stringify({message: inputText})
    });

        const responseData = await response.json();

        appendMessage("bot", responseData);
    }

    catch(error){
        appendMessage("bot", error);
    }
});