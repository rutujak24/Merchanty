function leaveInput(el) {
		if (el.value.length > 0) {
				if (!el.classList.contains('active')) {
						el.classList.add('active');
				}
		} else {
				if (el.classList.contains('active')) {
						el.classList.remove('active');
				}
		}
}

var inputs = document.getElementsByClassName("m-input");
for (var i = 0; i < inputs.length; i++) {
		var el = inputs[i];
		el.addEventListener("blur", function() {
				leaveInput(this);
		});
}

function shipping() {

	var uname = sessionStorage.getItem('uname');
	console.log(uname);

    var name = document.getElementById('first').value;
    var email = document.getElementById('last').value;
    var contact = document.getElementById('Contact').value;
    var address = document.getElementById('address').value;
    var zip = document.getElementById('ZipCode').value;

    var request = new XMLHttpRequest();
    var req_url = 'http://localhost:5000/shipping?email=' + email + '&name=' + name + '&contact=' + contact + '&address=' + address + '&zip=' + zip + '&uname=' + uname;
    // console.log(req_url);
    request.open('GET', req_url, true);
    request.onload = function () {
        var data = this.response;
        console.log(data);

        if(data == 'Good'){
            window.location.href = 'DBMS_project.html';
        }
        else{
            window.location.href = 'input_page.html';
        }
    }
    request.send();
}