$('#registerSubmit').on('click', function (e) {
    e.preventDefault();
    let username = $('#username').val();
    let email = $('#email').val();
    let password = $('#password').val();
    let cfpassword = $('#confirmPassword').val();


    if (username != '' && password != '' && cfpassword != '') {
        if (password != cfpassword) {
            $('#msg').html('<span style="color: #eb6383">비밀번호가 일치하지 않아요 :)</span>')
        } else {
            $.ajax({
                type: "POST",
                url: '/user/register',
                data: {'username': username, 'email': email, 'password': password},
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