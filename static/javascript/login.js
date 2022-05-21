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
                    if (data.result == 'SUCCESS') {
                        alert(data.msg)
                        $('#exampleModal').modal('hide') //로그인 후 alert 확인 클릭하면 modal 숨기기
                        const logoutButton = `<a id="logoutButton" type="button" onclick="">logout</a>`
                        $('#loginButton').replaceWith(logoutButton) //로그인 되면 해당 버튼 로그아웃으로 변경
                    } else {
                        alert(data.msg)
                    }
                }, statusCode: {
                    400: function () {
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

$('#signup .email').blur(function () {
    let email = $($('.email')[1]).val();
    let regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i; //이메일 정규식

    if (!regex.test(email)) {
        $('#email-warning').html('<span style="color: #eb6383">유요한 이메일 형식이 아닙니다</span>')
    } else {
        $.ajax({
            type: "GET",
            url: '/user/check?email=' + email,
            data: {},
            success: function (res) {
                if (res.result == 'FAIL') {
                    $('#email-warning').html('<span style="color: #eb6383">이미 사용 중인 이메일입니다.</span>')
                }
            }
        })
    }
})

$('#signup .email').focus(function () {
    $('#email-warning').html('')
})

$('#registerSubmit').on('click', function (e) {
    e.preventDefault()

    let username = $('#signup .username').val();
    let email = $($('.email')[1]).val();
    let password = $('#signup .password').val();
    let cfpassword = $('#signup .confirmPassword').val();

    if (username != '' && password != '' && cfpassword != '') {
        if (password != cfpassword) {
            $('#email-warning').html('<span style="color: #eb6383">비밀번호가 일치하지 않아요 :)</span>')
        } else {
            $.ajax({
                type: "POST",
                url: '/user/register',
                data: {'username': username, 'email': email, 'password': password},
                success: function (data) {
                    if (data.result == 'SUCCESS') {
                        let inputs = document.querySelectorAll('#regForm input')
                        for(let i = 0; i < inputs.length; i++){
                            inputs[i].value = null
                        }

                        $('#signup').removeClass('show active')
                        $('#signup-tab').removeClass('active')
                        $('#login').addClass('show active')
                        $('#login-tab').removeClass('active')
                    }
                }
            })
        }
    } else {
        $('#email-warning').html('<span style="color: #eb6383">모든 입력란을 채워주세요</span>')
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