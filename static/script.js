const chatBox = document.getElementById("chatBox");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");

function appendMessage(sender, text) {
    const chatDiv = document.createElement("div");

    chatDiv.classList.add("message", sender);

    chatDiv.innerHTML = DOMPurify.sanitize(marked.parse(text));

    chatBox.appendChild(chatDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function typingBubble(){
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "typing", "bot");
    typingDiv.innerText = "AI is typing...";
    chatBox.appendChild(typingDiv)
    chatBox.scrollTop = chatBox.scrollHeight;
    
    return typingDiv;
}

chatForm.addEventListener("submit", async function (event){
    event.preventDefault();

    const inputText = userInput.value;

    appendMessage("user", inputText);

    if (!(inputText)) return;

    userInput.value = "";

    typingDiv = typingBubble();

    try{
        const response = await fetch("/botchat", {
            method: "POST",
            headers: {"Content-Type" : "application/json"},
            body: JSON.stringify({message: inputText})
    });

        const data = await response.json();

        chatBox.removeChild(typingDiv);

        appendMessage("bot", data.response);
    }

    catch(error){
        appendMessage("bot", "Error: bot encountered an unknown error");
    }
});