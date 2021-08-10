console.log("js");
let val;
function showfake()
{
    document.getElementById("real").style.visibility="hidden";
    document.getElementById("fakepara").style.visibility="visible";
}
function showreal()
{
    document.getElementById("fake").style.visibility="hidden";
    document.getElementById("realpara").style.visibility="visible";
}
// val=1;
if (val==0){
    showfake();
}
else if(val==1){
    showreal();
}
