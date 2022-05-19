$(document).ready(function () {
    $('#loginSubmit').on('click', function (e) {
        e.preventDefault();
        let email = $('#email').val();
        let password = $('#password').val();

        let regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i; //이메일 정규식

        if (email != '' && password != '') {
            if (!regex.test(email)) {
                $('#msg').html('<span style="color: #eb6383">유요한 이메일 형식이 아닙니다</span>')
            } else {
                $.ajax({
                    method: "POST",
                    url: '/user/login',
                    contentType: 'application/json; charset=UTF-8',
                    data: JSON.stringify({'email': email, 'password': password}),
                    dataType: 'json',
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
            }
        } else {
            $('#msg').html('<span style="color: #eb6383">모든 입력란을 채워주세요</span>')
        }
    })
})
