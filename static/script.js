const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");
const attachBtn = document.getElementById("attachBtn");
const attachMenu = document.getElementById("attachMenu");
const menuUploadBtn = document.getElementById("menuUploadBtn");
const menuCancelBtn = document.getElementById("menuCancelBtn");
const pdfFileInput = document.getElementById("pdfFile");

// Toggle floating attachment menu
if (attachBtn && attachMenu) {
    attachBtn.addEventListener("click", function(e) {
        e.stopPropagation();
        attachMenu.classList.toggle("hidden");
    });
}

// Close attachment menu when clicking cancel
if (menuCancelBtn && attachMenu) {
    menuCancelBtn.addEventListener("click", function(e) {
        e.stopPropagation();
        attachMenu.classList.add("hidden");
    });
}

// Trigger hidden file input click when clicking upload pdf in the menu
if (menuUploadBtn && pdfFileInput) {
    menuUploadBtn.addEventListener("click", function(e) {
        e.stopPropagation();
        if (attachMenu) {
            attachMenu.classList.add("hidden");
        }
        pdfFileInput.click();
    });
}

// Close attachment menu when clicking outside
document.addEventListener("click", function(e) {
    if (attachMenu && !attachMenu.classList.contains("hidden")) {
        if (!attachBtn.contains(e.target) && !attachMenu.contains(e.target)) {
            attachMenu.classList.add("hidden");
        }
    }
});

// Trigger automatic upload on file input change
if (pdfFileInput) {
    pdfFileInput.addEventListener("change", async function() {
        if (pdfFileInput.files.length > 0) {
            await uploadPDF();
        }
    });
}

messageInput.addEventListener("keydown", function(e){

    if(e.key==="Enter" && !e.shiftKey){

        e.preventDefault();
        sendMessage();

    }

});

messageInput.addEventListener("input",()=>{

    messageInput.style.height="40px";
    messageInput.style.height=messageInput.scrollHeight+"px";

});

function addUserMessage(text){

    const div=document.createElement("div");

    div.className="flex justify-end message";

    div.innerHTML=`
    
    <div class="max-w-[70%] bg-blue-600 text-white px-6 py-4 rounded-3xl rounded-br-md shadow-xl">

        ${text}

    </div>

    `;

    chatBox.appendChild(div);

    chatBox.scrollTop=chatBox.scrollHeight;

}

function addBotMessage(text){

    const div=document.createElement("div");

    div.className="flex justify-start message";

    div.innerHTML=`

    <div class="glass max-w-[75%] text-white px-6 py-5 rounded-3xl rounded-bl-md">

        ${text}

    </div>

    `;

    chatBox.appendChild(div);

    chatBox.scrollTop=chatBox.scrollHeight;

}

function typingIndicator(){

    const div=document.createElement("div");

    div.id="typing";

    div.className="flex justify-start message";

    div.innerHTML=`

    <div class="glass px-6 py-5 rounded-3xl text-white">

        <span class="animate-pulse">●</span>

        <span class="animate-pulse delay-100">●</span>

        <span class="animate-pulse delay-200">●</span>

    </div>

    `;

    chatBox.appendChild(div);

    chatBox.scrollTop=chatBox.scrollHeight;

}

async function sendMessage(){

    const text=messageInput.value.trim();

    if(text==="") return;

    if(chatBox.innerHTML.includes("Welcome back")){

        chatBox.innerHTML="";

    }

    addUserMessage(text);

    messageInput.value="";
    messageInput.style.height="40px";

    typingIndicator();

    try {
        const response=await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:text
            })

        });

        const data=await response.json();

        const typingEl = document.getElementById("typing");
        if (typingEl) {
            typingEl.remove();
        }

        addBotMessage(data.response);
    } catch (error) {
        console.error("Error sending message:", error);
        const typingEl = document.getElementById("typing");
        if (typingEl) {
            typingEl.remove();
        }
        addBotMessage("Sorry, I encountered an error connecting to the server. The server might still be starting up or loading models. Please try again in a few seconds.");
    }

}

async function uploadPDF() {

    const fileInput = document.getElementById("pdfFile");

    if (fileInput.files.length === 0) {
        alert("Please select a PDF.");
        return;
    }

    const formData = new FormData();

    formData.append("pdf", fileInput.files[0]);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    alert(data.message);

    // Clear input value to allow uploading the same file again
    fileInput.value = "";
}