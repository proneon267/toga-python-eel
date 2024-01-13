async function EnableFan(){
	let result = await eel.EnableFan()();
	if(result == 1){
		document.getElementById("ShortMsg").innerHTML = "Enabled";
		document.getElementById("LongMsg").innerHTML = "The Fan is enabled";
	}
}
async function DisableFan(){
	let result = await eel.DisableFan()();
	if(result == 2){
		document.getElementById("ShortMsg").innerHTML = "Disabled";
		document.getElementById("LongMsg").innerHTML = "The Fan is disabled";
	}
}
