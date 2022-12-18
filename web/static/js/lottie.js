/*jshint esversion: 6 */
"use strict";

let lotties = document.getElementsByClassName("lottie");

for ( let i = 0; i < lotties.length; i++ ){

    if (lotties[i].getAttribute("lottie") === "on-hover"){
        let animation = bodymovin.loadAnimation({
                container : lotties[i],
                path: lotties[i].getAttribute("lottie-path"),
                render: "svg",
                loop: true,
                autoplay: false,
                name: "lottie animation" + String(i),
            });

        if (lotties[i].hasAttribute("lottie-speed")){
            animation.setSpeed(lotties[i].getAttribute("lottie-speed"));
        }

        function onMouseEnter(){animation.play();}
        function onMouseLeave(){animation.pause();}

        lotties[i].addEventListener("mouseenter", onMouseEnter);
        lotties[i].addEventListener("mouseleave", onMouseLeave);
    }

    else if (lotties[i].getAttribute("lottie") === "loop"){
            let animation = bodymovin.loadAnimation({
                container : lotties[i],
                path: lotties[i].getAttribute("lottie-path"),
                render: "svg",
                loop: true,
                autoplay: true,
                name: "lottie animation" + String(i),
            });

            if (lotties[i].hasAttribute("lottie-speed")){
                animation.setSpeed(lotties[i].getAttribute("lottie-speed"));
            }

            animation.play();
    }

    else if (lotties[i].getAttribute("lottie") === "on-hover-loop"){
        let animation = bodymovin.loadAnimation({
                container : lotties[i],
                path: lotties[i].getAttribute("lottie-path"),
                render: "svg",
                loop: true,
                autoplay: false,
                name: "lottie animation" + String(i),
            });

        if (lotties[i].hasAttribute("lottie-speed")){
            animation.setSpeed(lotties[i].getAttribute("lottie-speed"));
        }

        function onMouseEnter(){animation.play();}
        function onMouseLeave(){animation.pause();}

        lotties[i].addEventListener("mouseenter", onMouseEnter);
        lotties[i].addEventListener("mouseleave", onMouseLeave);
    }
}