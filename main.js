
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.className='dark';
} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
    document.body.className='light';
}

function toggleTheme() {
    let className = document.body.className;
    
    if (className=='dark') {
        document.body.className='light';

    } else if (className=='light') {
        document.body.className='dark';
    }
}

function hideNav() {
    var x = document.getElementById("nav-list");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
