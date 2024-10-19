const url = window.location.href
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


function first_contact_block() {
    var name = document.getElementById("name1").value;
    var number = document.getElementById("number1").value;
    $.ajax({
        type: "POST",
        url: url,
        data: {
            "csrfmiddlewaretoken": csrf,
            'name': name,
            'number': number,
        },
        success: (res)=> {
            if (res.status == 'success') {
                alert('Заявка успешно отправлена!');
                document.getElementById("name1").value = '';
                document.getElementById("number1").value = '';
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


function second_contact_block() {
    var name = document.getElementById("name2").value;
    var number = document.getElementById("number2").value;
    $.ajax({
        type: "POST",
        url: url,
        data: {
            "csrfmiddlewaretoken": csrf,
            'name': name,
            'number': number,
        },
        success: (res)=> {
            if (res.status == 'success') {
                alert('Заявка успешно отправлена!');
                document.getElementById("name2").value = '';
                document.getElementById("number2").value = '';
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