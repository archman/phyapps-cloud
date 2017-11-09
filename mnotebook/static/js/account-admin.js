$(function() {
    // delete user
    $(".btn-del-user").click(function() {
        var url = $(this).data('url');
        $.ajax({
            type: "DELETE",
            url: url,
            success: function() {
                alert("User Deleted");
                location.reload();
            },
            error: function() {
                alert("Delete Failed");
            }
        });
    });

    // edit user
    $(".btn-edit-user").click(function() {
        var uname = $(this).data('uname');
        var cid   = $(this).data('cid');
        var desc  = $(this).data('desc');
        var curl  = $(this).data('curl');
        var url  = $(this).data('url');
        $(".modal-body #username").val(uname);
        $(".modal-body #container_id").val(cid);
        $(".modal-body #description").val(desc);
        $(".modal-body #server_url").val(curl);
        $(".modal-body #user_url").val(url);
    });

    // submit update user
    $(".submit-update-user").click(function() {
        var uname = $(".modal-body #username").val();
        var cid   = $(".modal-body #container_id").val();
        var desc  = $(".modal-body #description").val();
        var curl  = $(".modal-body #server_url").val();
        var url   = $(".modal-body #user_url").val();
        var data  = {'name': uname, 'description': desc,
                     'container_id': cid, 'server_url': curl};
        $.ajax({
            type: "PUT",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function() {
                alert("User Updated");
                location.reload();
            },
            error: function() {
                alert("Update Failed");
            }
        });
    });

    // submit create user
    $(".submit-create-user").click(function() {
        uname = $(".modal-body #new_username").val();
        cid   = $(".modal-body #new_container_id").val();
        desc  = $(".modal-body #new_description").val();
        curl  = $(".modal-body #new_server_url").val();
        url  = $(".open-create-user").data('url');
        var data = {'name': uname, 'description': desc,
                    'container_id': cid, 'server_url': curl};
        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function() {
                alert("User Created");
                location.reload();
            },
            error: function() {
                alert("Create Failed");
            }
        });
    });
});

$(function() {
    // delete admin
    $(".btn-del-admin").click(function() {
        var nickname = $(this).data('nickname');
        var url = $(this).data('url');
        var data = {'nickname': nickname};
        $.ajax({
            type: "DELETE",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function() {
                alert("Admin Deleted");
                location.reload();
            },
            error: function() {
                alert("Delete Failed");
            }
        });
    });

    // edit admin
    $(".btn-edit-admin").click(function () {
        var nickname = $(this).data('nickname');
        var email = $(this).data('email');
        var url = $(this).data('url');
        $(".modal-body #nickname").val(nickname);
        $(".modal-body #email").val(email);
    });

    // submit update admin
    $(".submit-update-admin").click(function() {
        var nickname = $(".modal-body #nickname").val();
        var password = $(".modal-body #password").val();
        var email    = $(".modal-body #email").val();
        var data = {'nickname': nickname, 'password': password,
                    'email': email};
        var url = $(".btn-edit-admin").data('url');
        $.ajax({
            type: "PUT",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function() {
                alert("Admin Updated");
                location.reload();
            },
            error: function() {
                alert("Update Failed");
            }
        });
    });

    // submit create admin
    $(".submit-create-admin").click(function() {
        var nickname = $(".modal-body #new_nickname").val();
        var password = $(".modal-body #new_password").val();
        var email    = $(".modal-body #new_email").val();
        var url  = $(".open-create-admin").data('url');
        var data = {'nickname': nickname, 'password': password,
                    'email': email};
        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function() {
                alert("Admin Created");
                location.reload();
            },
            error: function() {
                alert("Create Failed");
            }
        });
    });
});
