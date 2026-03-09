function translate(lang){

const id=window.location.pathname.split("/")[2]

fetch(`/translate/${id}/${lang}`)

.then(res=>res.json())

.then(data=>{

document.getElementById("description").innerText=data.translation

})

}

function ask(){

const question=document.getElementById("question").value

ffetch(`/ask/` + window.location.pathname.split("/")[2],{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({
question:question,
context:context
})

})

.then(res=>res.json())

.then(data=>{

document.getElementById("answer").innerText=data.answer

speak(data.answer)

})

}

function startVoice(){

const recognition=new webkitSpeechRecognition()

recognition.onresult=function(event){

document.getElementById("question").value=event.results[0][0].transcript

ask()

}

recognition.start()

}

function speak(text){

const speech=new SpeechSynthesisUtterance(text)

speechSynthesis.speak(speech)

}