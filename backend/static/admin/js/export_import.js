function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(document).on('click', '#btn_export_sample', function (e) {
    e.preventDefault();
    let url = $(this).data('url');
    let choice_data = $('#choice_data').html();
    let field_list = $('#field_list').html();

    console.log(JSON.parse(field_list));
    let data = {
        field_list: JSON.parse(field_list),
        choice_data: JSON.parse(choice_data)
    };
    $.ajax({
        type: 'post',
        data: JSON.stringify(data),
        dataType: 'JSON',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            // console.log(res.blob());
            console.log('file downloading');
            let blob = new Blob([data]);

            let file_url = url.createObjectURL(blob);
            let element = document.createElement('a');
            element.style.display = 'none';
            element.href = file_url;
            // element.target = '_blank';
            element.download = 'sample.csv';
            document.body.appendChild(element);
            element.click();
            window.URL.revokeObjectURL(file_url);
            alert('your file has downloaded!');
        },
        error: function (err) {
            console.log(err);
            console.log('file downloading');
            let url = window.URL || window.webkitURL;
            let blob = new Blob([err.responseText]);

            let file_url = url.createObjectURL(blob);
            let element = document.createElement('a');
            element.style.display = 'none';
            element.href = file_url;
            // element.target = '_blank';
            element.download = 'sample.csv';
            document.body.appendChild(element);
            element.click();
            alert('your file has downloaded!');
        }
    })
});

$(document).on('click', '#btn_export_instruction_sample', function (e) {
    e.preventDefault();
    let url = $(this).data('url');
    let field_list = $('#field_list').html();

    console.log(JSON.parse(field_list));
    let data = {
        field_list: JSON.parse(field_list)
    };
    $.ajax({
        type: 'post',
        data: JSON.stringify(data),
        dataType: 'JSON',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            // console.log(res.blob());
            console.log('file downloading');
            let blob = new Blob([data]);

            let file_url = url.createObjectURL(blob);
            let element = document.createElement('a');
            element.style.display = 'none';
            element.href = file_url;
            // element.target = '_blank';
            element.download = 'sample.csv';
            document.body.appendChild(element);
            element.click();
            window.URL.revokeObjectURL(file_url);
            alert('your file has downloaded!');
        },
        error: function (err) {
            console.log(err);
            console.log('file downloading');
            let url = window.URL || window.webkitURL;
            let blob = new Blob([err.responseText]);

            let file_url = url.createObjectURL(blob);
            let element = document.createElement('a');
            element.style.display = 'none';
            element.href = file_url;
            // element.target = '_blank';
            element.download = 'sample.csv';
            document.body.appendChild(element);
            element.click();
            alert('your file has downloaded!');
        }
    })
});
