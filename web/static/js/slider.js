/*jshint esversion: 6 */
"use strict";

const slider = document.getElementById("slider");
const sliderImage = document.getElementsByClassName("image-div")[1];
const sliderRect = document.getElementById("image-container").getBoundingClientRect();
const sliderTransitionDuration = 750;
let sliderOpacity = 1;
let inSlider = true;

function slider_on_mouse_move(e) {

        inSlider = true;

        let currSliderOpacity = sliderOpacity * sliderTransitionDuration;

        let functionStartTime = Date.now();

        let timer = setInterval(function() {
                if (inSlider){
                        let timePassed = currSliderOpacity + (Date.now() - functionStartTime);

                        if (timePassed >= sliderTransitionDuration) {
                                clearInterval(timer);
                                return;
                        }
                        sliderOpacity = timePassed / sliderTransitionDuration;
                        sliderImage.style.opacity = sliderOpacity;
                }
        }, 10);

        let x = e.clientX;
        let left = sliderRect.left + window.scrollX;
        let new_val = (x-left) * 100 / document.getElementById("image-container").offsetWidth;

        if (new_val < 1){
                new_val = 0;
        }

        else if (new_val > 99){
                new_val = 100;
        }

        slider.setAttribute('value', new_val);
        sliderImage.style.clipPath = "inset(0 " + (100-new_val) + "% 0 0)";
}

function slider_on_mouse_leave(e) {

        inSlider = false;

        let onMouseLeaveOpacity = sliderOpacity * sliderTransitionDuration;

        let start = Date.now();

        let timer = setInterval(function() {
                if (!inSlider){
                        let timePassedOpacity = onMouseLeaveOpacity - (Date.now() - start);

                        if (timePassedOpacity <= 0) {
                                clearInterval(timer);
                                return;
                        }
                        sliderOpacity = timePassedOpacity / sliderTransitionDuration;
                        sliderImage.style.opacity = sliderOpacity;
                }
        }, 10);
}