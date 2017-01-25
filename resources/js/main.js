var queue_last_id = -1;
var queue_remove_timeouts = {};
var queue_ids = new Set();
var queue_remove_ids = new Set();

jsh.addEventListener("ready", function() {
    build_dom();
    bind_listeners();

    if (window.location.href.indexOf("#") == -1) jsh.pages["syllabus"].open();
});

function build_dom() {
    var nav = jsh.get("#nav_inner");
    for (var page in jsh.pages) {
        if (jsh.pages.hasOwnProperty(page)) {
            var nav_text = jsh.pages[page].div.getAttribute("nav_text");
            if (!nav_text) continue;

            var nav_item = document.createElement("span");
            nav_item.classList.add("nav_item");
            nav_item.innerText = nav_text;
            nav_item.setAttribute("target", jsh.pages[page].name);
            nav_item.id = "nav_" + jsh.pages[page].div.id;
            nav.appendChild(nav_item);

            nav_item.addEventListener("click", function(e) {
                var page_name = e.target.getAttribute("target");
                if (jsh.pages[page_name]) {
                    jsh.pages[page_name].open();
                }
            });
        }
    }

    setInterval(function() {
        new jsh.Request({
            url: "./db/queue.py",
            parse_json: true,
            data: {
                action: "get",
                last_id: queue_last_id
            },
            callback: function(result) {
                var queue = jsh.get("#queue");
                for (var i = 0; i < result.data.length; i++) {
                    var id = result.data[i][0];
                    if (queue_ids.has(id)) {
                        queue_remove_ids.delete(id);
                        continue;
                    }
                    queue_ids.add(id);
                    queue_last_id = id;

                    var queue_item = document.createElement("div");
                    queue_item.classList.add("queue_item");
                    queue_item.setAttribute("id", "queue_item_" + id);

                    var queue_item_check = document.createElement("span");
                    queue_item_check.classList.add("queue_item_check");

                    var queue_item_name = document.createElement("span");
                    queue_item_name.classList.add("queue_item_name");
                    queue_item_name.innerText = result.data[i][1];

                    queue_item.appendChild(queue_item_check);
                    queue_item.appendChild(queue_item_name);
                    queue.appendChild(queue_item);

                    queue_item.addEventListener("click", queue_item_handler);
                    queue_item.setAttribute("uid", result.data[i][0]);
                }

                for (var iter = queue_remove_ids.values(), val= null; id=iter.next().value;) {
                    var item = jsh.get("#queue_item_" + id);
                    if (item) {
                        remove_queue_item(item);
                    }
                    queue_ids.delete(id);
                }
                queue_remove_ids = new Set();
            }
        }).send();
    }, 2000);

    setInterval(function() {
        queue_last_id = -1;
        queue_remove_ids = new Set(queue_ids);
    }, 5000);
}

function queue_item_handler(e) {
    if (!e.target.classList.contains("queue_item")) {
        e.target.parentNode.click();
    } else {
        var check = e.target.childNodes[0];
        var id = parseInt(e.target.getAttribute("uid"));
        if (!check.classList) check = e.target.childNodes[1];
        if (check.classList.contains("queue_item_checked")) {
            check.classList.remove("queue_item_checked");
            if (queue_remove_timeouts[id]) {
                clearTimeout(queue_remove_timeouts[id]);
            }
        } else {
            check.classList.add("queue_item_checked");
            queue_remove_timeouts[id] = setTimeout(function() {
                new jsh.Request({
                    url: "./db/queue.py",
                    parse_json: true,
                    data: {
                        action: "remove",
                        id: id
                    },
                    callback: function(result) {
                        if (result.success) {
                            remove_queue_item(e.target);
                        }
                    }
                }).send();
            }, 5000)
        }
    }
}

function remove_queue_item(queue_item) {
    queue_item.classList.add("queue_item_exit");
    setTimeout(function() {
        queue_item.remove();
    }, 500);
}

function bind_listeners() {
    var parallax_bg = jsh.get(".parallax_bg");
    window.addEventListener("scroll", function() {
        for (var i = 0; i < parallax_bg.length; i++) {
            parallax_bg[i].style.backgroundPositionY = (document.body.scrollTop / 2) + "px";
        }
    });

    var homework_list_items = jsh.get(".homework_list_item");
    for (var i = 0; i < homework_list_items.length; i++) {
        homework_list_items[i].addEventListener("click", function(e) {
            if (!e.target.classList.contains("homework_list_item")) {
                e.target.parentNode.click();
                return;
            }
            var resources = JSON.parse(e.target.getAttribute("resources"));
            open_homework(resources);
        });
    }

    jsh.get("#help_queue_input").addEventListener("keypress", function(e) {
        if (e.keyCode == 13) {
            new jsh.Request({
                url: "./db/queue.py",
                parse_json: true,
                data: {
                    action: "insert",
                    name: e.target.value
                },
                callback: function(result) {
                    e.target.value = "";
                }
            }).send();
        }
    });
}

function open_homework(resources) {
    if (resources.length > 1) {
        new jsh.Alert({
            title: "This assignment has multiple resources:",
            button_text: "done",
            message: function() {
                var message = "<ul>";
                for (var i = 0; i < resources.length; i++) {
                    message += jsh.str("<li><a class='alert_link' target='_blank' href='./downloads/{}'>{}</a></li>", resources[i], resources[i])
                }
                message += "</ul>";
                return message;
            }()
        }).open();
    } else {
        window.open("./downloads/" + resources[0],'_blank');
    }
}
