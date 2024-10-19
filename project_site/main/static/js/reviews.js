const url = window.location.href

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


function make_review() {
    var name = document.getElementById("name").value;
    var review = document.getElementById("review").value;
    $.ajax({
        type: "POST",
        url: url,
        data: {
            "csrfmiddlewaretoken": csrf,
            'name': name,
            'review': review,
        },
        success: (res)=> {
            if (res.status == 'success') {
                alert('Ваш отзыв отправлен на модерацию!');
                document.getElementById("name").value = '';
                document.getElementById("review").value = '';
            }
            else if (res.status == 'short') {
                alert('Ваш отзыв слишком короткий!');
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