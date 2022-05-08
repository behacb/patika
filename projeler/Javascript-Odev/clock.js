function showTime(){
    var date = new Date();
    
    var d=date.getDate();
    var mo=date.getMonth();
    var y=date.getFullYear();
    var h = date.getHours();
    var m = date.getMinutes();
    var s = date.getSeconds();
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    var history= d+"."+(mo+1)+"."+y;
    var time = + h+":"+m+":"+s;
    document.getElementById("myDateDisplay").innerText=history;
    document.getElementById("myDateDisplay").textContent=history;

    document.getElementById("myClockDisplay").innerText=time;
    document.getElementById("myClockDisplay").textContent=time;
    setTimeout(showTime, 1000);
}
showTime();