const websocket = new WebSocket("ws://127.0.0.1:8000/ws");

const chatBox = document.getElementById("chat-box");

websocket.onmessage = function(event) {

    addMessage(event.data, "bot");
};

function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");

    websocket.send(message);

    input.value = "";
}

function addMessage(message, sender) {

    const div = document.createElement("div");

    div.classList.add("message");

    div.classList.add(sender);

    // Render markdown
    div.innerHTML = marked.parse(message);

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

/* Enter key support */

document
    .getElementById("message")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            sendMessage();
        }
    });