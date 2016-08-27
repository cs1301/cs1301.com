jsh.addEventListener("ready", function() {
    build_dom();
    bind_listeners();
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
}

function open_homework(resources) {
    if (resources.length > 1) {
        new jsh.Alert({
            title: "This assignment has multiple resources:",
            button_text: "done",
            message: function() {
                var message = "<ul>";
                for (var i = 0; i < resources.length; i++) {
                    message += jsh.str("<li><a class='alert_link' href='./downloads/{}'>{}</a></li>", resources[i], resources[i])
                }
                message += "</ul>";
                return message;
            }()
        }).open();
    } else {
        window.location = "./downloads/" + resources[0];
    }
}