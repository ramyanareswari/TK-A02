//make sure window is loaded
window.onload = function () {

    console.log('hello world')

    const modalBtns = [...document.getElementsByClassName('modal-button')];
    const modalBody = document.getElementById('modal-body-confirm');
    const startBtn = document.getElementById('start-button');
    const goback1 = document.getElementById("goback1");
    const goback2 = document.getElementById("goback2");
    const url = window.location.href;

    // Listener in Goback Button
    if(goback1 != null) {
        goback1.addEventListener('click', ()=> {
        window.location.href = '/'
        })
    }

    // Listener for GoBack Button
    if(goback2 != null){
        goback2.addEventListener('click', ()=> {
        window.location.href = '/mini-quiz/';
        })
    }

    modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=> {
        const name = modalBtn.getAttribute('data-quiz')
        const numOfQuestions = modalBtn.getAttribute('data-questions')
        const scoreToPass = modalBtn.getAttribute('data-pass')
        const time = modalBtn.getAttribute('data-time')

        // Add this html tag to modalBody
        modalBody.innerHTML = `
            <div class="header-text-muted h10 mb-3">Are you sure want to begin <b>"${name}"</b>?</div>
            <div class=text-muted>
                <ul>
                    <li>Test Name : ${name}</li>
                    <li>Number of Question : ${numOfQuestions}</li>
                    <li>Duration : ${time} min</li>
                </ul>
            </div>`;

        startBtn.addEventListener('click', ()=> {
            window.location.href = url
        })
    })
)}