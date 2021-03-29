
        function ajaxSend(url, params) {
            // Отправляем запрос
            fetch(`${url}?${params}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
                .then(response => response.json())
                .then(json => render(json))
                .catch(error => console.error(error))
        }

        //Filter movies
        const forms = document.querySelector('form[name=filter]');

        forms.addEventListener('submit', function (e) {
           // Получаем данные из формы
           e.preventDefault();
           let url = this.action;
           let params = new URLSearchParams(new FormData(this)).toString();
           ajaxSend(url, params);
        });

        function render(data) {
           // Рендер шаблона
           let template = Hogan.compile(html);
           let output = template.render(data);

           const div = document.querySelector('.container>.default_page');
           div.innerHTML = output;
        }

        // Add star rating
        const rating = document.querySelector('form[name=rating]');

        rating.addEventListener("change", function (e) {
            // Получаем данные из формы
            let data = new FormData(this);
            fetch(`${this.action}`, {
                method: 'POST',
                body: data
            })
                .then(response => alert("Рейтинг установлен"))
                .catch(error => alert("Ошибка"))
        });


let html = '\
        {{#sts}}\
        < div class= "col-sm-12 col-md-12 px-0 px-md-5 py-md-4 mt-2 users text-center" >\
        <div class="row px-3 mt-3 mb-4 text-sm-left">\
        <div class="col-sm-2 px-0 ml-md-3">\
        <img class="img-fluid" src="/media/' + data[0][i].student_image + '" alt="avatar" name="inpFile"\
        id="inpFile2">\
        </div>\
        <div class="col-sm-4 col-md-6 pt-2 offset-sm-1 offset-md-2 offset-lg-1">\
        <h5 class="font-size-20">' + data[0][i].first_name + ' ' + data[0][i].last_name + '</h5>\
        <p class="text-light font-size-14">' + data[0][i].direction + '</p>\
        </div>\
        </div>\
        <div class="row px-4 px-md-3 d-flex flex-column align-items-center flex-sm-row">\
        <div class="px-2 mb-3 mb-md-0 col-md-4 col-sm-4 col-10 img-project-div">\
        <img src="/media/{{data[1][i].project_pick}}" class="img-fluid img-project" alt="kkk">\
        </div>\
        </div>\
        <div class="row px-4 px-md-3 mt-5 mb-5 mb-md-0 d-flex flex-column align-content-center flex-sm-row justify-content-sm-between">\
        <div class="col-sm-6 mb-4 mb-md-0 text-center text-sm-left">\
        <span>Навыки</span>\
        <br>\
        <span class="text-light font-size-14"> ' + data[0][i].skills + ' </span>\
        </div>\
        <div class="col-sm-6 text-center text-sm-right">\
        <a class="btn btn-danger rounded-15 px-4 py-2" href="/student_card/' + data[0][i].id + '">Подробнее</a>\
        </div>\
        </div>\
        </div>\
        {{/sts}}'