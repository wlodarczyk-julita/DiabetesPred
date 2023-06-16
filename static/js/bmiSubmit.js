document.addEventListener("DOMContentLoaded", function() {
    const bmiSubmit = document.querySelector(".bmiSubmit");
    const bmiSubmitDescribe = document.querySelector(".bmiSubmitDescribe");
    console.log(bmiSubmit.textContent);
    console.log(bmiSubmitDescribe.textContent);
    if(bmiSubmitDescribe.textContent == 'Niedowaga') {
        const container1 = document.querySelector(".container1");
      //  container1.style.backgroundColor = "WhiteSmoke";
        container1.style.fontWeight ="800"
        bmiSubmitDescribe.style.color = "#638475"
    }  else if(bmiSubmitDescribe.textContent == 'Waga w normie') {
        const container2 = document.querySelector(".container2");
      //  container2.style.backgroundColor = "WhiteSmoke";
        container2.style.fontWeight ="800"
        bmiSubmitDescribe.style.color = "#90e39a"
    } else if(bmiSubmitDescribe.textContent == 'Nadwaga') {
        const container3 = document.querySelector(".container3");
      //  container3.style.backgroundColor = "#ddf093";
        container3.style.fontWeight ="800"
    } else if(bmiSubmitDescribe.textContent == 'Otyłość') {
        const container4 = document.querySelector(".container4");
       // container4.style.backgroundColor = "#f6d0b1";
        container4.style.fontWeight ="800"
    } else {
        const container5 = document.querySelector(".container5");
       // container5.style.backgroundColor = "#ce4760";
        container5.style.fontWeight ="800"
    }
  });