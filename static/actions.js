
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

function fetch_func() {
        const id = document.getElementById("ID").value;
        const url = `https://reqres.in/api/users/${id}`
        fetch(url)
            .then(response => response.json())
            .then(value => {
                document.getElementById('user_container').innerHTML = `
            <h3>${value.data["first_name"]} ${value.data["last_name"]}</h3>
            <p>${value.data["email"]}"</p>
            <img src="${value.data["avatar"]}" alt="avatar"/>
            `
            })

    }

  function message_to_user() {

  alert("DB changed successfully");

  }

