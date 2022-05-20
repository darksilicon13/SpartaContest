$('#loginSubmit').on('click', function (e) {
    e.preventDefault();
    let email = $('.email').val();
    let password = $('.password').val();

    let regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i; //이메일 정규식

    if (email != '' && password != '') {
        if (!regex.test(email)) {
            $('#msg').html('<span style="color: #eb6383">유요한 이메일 형식이 아닙니다</span>')
        } else {
            $.ajax({
                type: "POST",
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
        }
    } else {
        $('#msg').html('<span style="color: #eb6383">모든 입력란을 채워주세요</span>')
    }
})

$('#registerSubmit').on('click', function (e) {
    e.preventDefault();
    let username = $('.username').val();
    let email = $('.email').val();
    let password = $('.password').val();
    let cfpassword = $('.confirmPassword').val();

    let regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i; //이메일 정규식

    if (username != '' && password != '' && cfpassword != '') {
        if (password != cfpassword) {
            $('#msg').html('<span style="color: #eb6383">비밀번호가 일치하지 않아요 :)</span>')
        } else if (!regex.test(email)) {
            $('#msg').html('<span style="color: #eb6383">유요한 이메일 형식이 아닙니다</span>')
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


//Login Modal
    let key = "${param.key}";
    console.log(key);
    if (key === "userinfo") {

        $("#myreview-tab").removeClass("active");
        $("#wishlist-tab").removeClass("active");
        $("#userinfo-tab").addClass("active");

        $("#myreview").removeClass("show active");
        $("#wishlist").removeClass("show active");
        $("#userinfo").addClass("show active");

    } else if (key === "myreview") {

        $("#wishlist-tab").removeClass("active");
        $("#userinfo-tab").removeClass("active");
        $("#myreview-tab").addClass("active");

        $("#userinfo").removeClass("show active");
        $("#wishlist").removeClass("show active");
        $("#myreview").addClass("show active");

    }