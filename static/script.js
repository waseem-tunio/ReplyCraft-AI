const generateBtn = document.getElementById("generateBtn");
const loading = document.getElementById("loading");
const reply = document.getElementById("reply");
const copyBtn = document.getElementById("copyBtn");

generateBtn.onclick = async () => {

    const email = document.getElementById("email").value.trim();
    const tone = document.getElementById("tone").value;

    if(email===""){

        alert("Please paste an email.");

        return;

    }

    loading.style.display="block";

    reply.textContent="";

    try{

        const response = await fetch("/generate",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                email,
                tone

            })

        });

        const data = await response.json();

        reply.textContent=data.reply;

    }

    catch(error){

        reply.textContent="Something went wrong.";

    }

    loading.style.display="none";

};

copyBtn.onclick=()=>{

    navigator.clipboard.writeText(reply.textContent);

    copyBtn.innerText="Copied!";

    setTimeout(()=>{

        copyBtn.innerText="Copy";

    },1500);

};