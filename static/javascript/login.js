$('#loginSubmit').on('click', function (e) {
    e.preventDefault();
    let email = $('#email').val();
    let password = $('#password').val();

    if (email != '' && password != '') {
        $.ajax({
            method: "POST",
            url: '/user/login',
            data: {'email': email, 'password': password},
            success: function (data) {
                $('#logForm').hide();
                $('#msg').html('<span style="color: #eb6383">로그인 성공!</span>');
            }, statusCode: {
                400: function () {
                    $('#msg').html('<span style="color: #eb6383">Bad request parameters</span>')
                },
            },
            error: function (err) {
                console.log(err);
            }
        })
    } else {
        $('#msg').html('<span style="color: #eb6383">모든 입력란을 채워주세요</span>')
    }
})
