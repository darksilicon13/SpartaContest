$(document).ready(function () {
    $('#registerSubmit').on('click', function (e) {
        e.preventDefault();
        let name = $('#username').val();
        let email = $('#email').val();
        let password = $('#password').val();
        let cfpassword = $('#confirmPassword').val();

        let regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i; //이메일 정규식

        if (username != '' && password != '' && cfpassword != '') {
            if (password != cfpassword) {
                $('#msg').html('<span style="color: #eb6383">비밀번호가 일치하지 않아요 :)</span>')
            } else if (!regex.test(email)) {
                $('#msg').html('<span style="color: #eb6383">유요한 이메일 형식이 아닙니다</span>')
            } else {
                $.ajax({
                    method: "POST",
                    url: '/register',
                    contentType: 'application/json; charset=UTF-8',
                    data: JSON.stringify({'name': name, 'email': email, 'password': password}),
                    dataType: 'json',
                    success: function (data) {
                        $('#regForm').hide();
                        $('#msg').html('<span style="color: #eb6383">회원가입 성공!</span>');
                    }, statusCode: {
                        400: function () {
                            $('#msg').html('<span style="color: #eb6383">Bad request parameters</span>')
                        },
                        409: function () {
                            $('#msg').html('<span style="color: #eb6383">이미 가입하신 회원입니다</span>')
                        }
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