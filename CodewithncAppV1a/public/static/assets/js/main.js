
function login(){
    var username = document.getElementById('loginUsername').value;
    var password = document.getElementById('loginPassword').value;
    var csrf = document.getElementById('csrfa').value;

    if (username == '' && password == ''){
        alert('Please enter username and password.');
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/access/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        'body' : JSON.stringify(data)
    }).then(result => result.json()).then(response => {
        console.log(response);

        if(response.status == 200){
            // window.location.href = '/';
            window.location.reload('/access/');
        }
        else{
            alert(response.message);
        }
    });
};




function register(){
    var username = document.getElementById('SignupUsername').value;
    var password = document.getElementById('SignupPassword').value;
    var csrf = document.getElementById('csrfr').value;

    if (username == '' && password == ''){
        alert('Please enter username and password.');
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/register/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        'body' : JSON.stringify(data)
    }).then(result => result.json()).then(response => {
        console.log(response);
        
        if(response.status == 200){
            alert(response.message)
        }
        else{
            alert(response.message);
        }
    });
};


function ud(){
    alert('Login and Signup Facility is currently not available for all users but will be available soon...');
}