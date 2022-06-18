
const activePage = window.location.pathname;
      
      
const navLinks = document.querySelectorAll('.nav_bar a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


function submit(x) {
  if (x.innerHTML=='Done'){
    location.href = "home_page.html"
  }
  else {
    document.getElementById("form").style.visibility='hidden';
    x.innerHTML = 'Done';
    var sub_title =  document.getElementById("h3");
    sub_title.innerHTML = 'Thank You!!' ;
    sub_title.style.fontSize ="xx-large";
    sub_title.animate([
        // keyframes
        { transform: 'translateY(300px)' },
        { transform: 'translateY(0px)' },
        { transform: 'translateY(300px)' },

      ], {
        // timing options
        duration: 3000,
        iterations: 3
    })
    alert("Thank you! We will contact you ASAP");
  }
}


function blackwhiteImg(x) {
  x.style.filter= "grayscale(100%)";
}

function colorImg(x) {
  x.style.filter= "grayscale(0%)";

}