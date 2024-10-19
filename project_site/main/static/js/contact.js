const url = window.location.href
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


function send_message() {
    var name = document.getElementById("name").value;
    var number = document.getElementById("number").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;
    var checked = document.getElementById('agreement').checked;
    $.ajax({
        type: "POST",
        url: url,
        data: {
            "csrfmiddlewaretoken": csrf,
            'name': name,
            'number': number,
            'email': email,
            'message': message,
            "checked": checked,
        },
        success: (res)=> {
            if (res.status == 'success') {
                alert('Заявка успешно отправлена!');
                document.getElementById("name").value = '';
                document.getElementById("number").value = '';
                document.getElementById("email").value = '';
                document.getElementById("message").value = '';
                document.getElementById("agreement").checked = false;
            }
            else if (res.status == 'not_checked') {
                alert('Подтвердите пользовательское соглашение!');
            }
            else if (res.status == 'fail') {
                alert('Заполните все поля!');
            }
        },
        error: (err)=> {
            console.log("error")
        }
    })
}