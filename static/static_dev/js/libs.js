$(function() {

  $.extend(true, $.magnificPopup.defaults, {
    fixedContentPos: true,
    mainClass: 'my-mfp-zoom-in',
    tClose: 'Закрыть (Esc) закрыть',
    tLoading: 'Загрузка...',
    gallery: {
      preload: [0,1],
      navigateByImgClick: true,
      tPrev: 'Предыдущее изображение (&larr;)',
      tNext: 'Следующее изображение (&rarr;)',
      tCounter: '<div class="mfp-counter">%curr% из %total%</div>'
    },
    image: {
      tError: '<a href="%url%">Изображение #%curr%</a> не найдено.'
    },
    ajax: {
      tError: '<a href="%url%">Ошибка при загрузке</a>'
    }
  });

  if ($('.main-slider').length) {
    var mainSlider = $('.main-slider').find('.slider .slider-carousel'),
        mainSliderDots = $('.main-slider').find('.slider .slider-dots');

    mainSlider.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
      mainSlider.removeClass('not-slick');

      function pad(d) {
        return (d < 10) ? '0' + d.toString() : d.toString();
      }

      var i = (currentSlide ? currentSlide : 0) + 1;

      mainSliderDots.find('.slider-dots-num')
        .html('<span class="active">' + pad(i) + '</span>/' + '<span>' + pad(slick.slideCount) + '</span>');
    }).slick({
      dots: true,
      arrows: false,
      slidesToShow: 1,
      slidesToScroll: 1,
      dotsClass: 'slider-dots-list',
      appendDots: mainSliderDots
    });
  }

  if ($('.main-expert').length) {
    var expertCarousel = $('.main-expert').find('.main-expert-carousel'),
        expertCarouselArrows = $('.main-expert').find('.carousel-arrows');

    expertCarousel.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
      expertCarousel.removeClass('not-slick');

      function pad(d) {
        return (d < 10) ? '0' + d.toString() : d.toString();
      }

      var i = (currentSlide ? currentSlide : 0) + 1;

      expertCarouselArrows.find('.carousel-slides-num')
        .html('<span class="active">' + pad(i) + '</span>/' + '<span>' + pad(slick.slideCount) + '</span>');
    }).slick({
      arrows: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      appendArrows: expertCarouselArrows
    });
  }

  if ($('.main-programs-slider').length) {
    var programsSlider = $('.main-programs-slider').find('.slider .slider-carousel'),
        programsSliderDots = $('.main-programs-slider').find('.slider .slider-dots');

    programsSlider.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
      programsSlider.removeClass('not-slick');

      function pad(d) {
        return (d < 10) ? '0' + d.toString() : d.toString();
      }

      var i = (currentSlide ? currentSlide : 0) + 1;

      programsSliderDots.find('.slider-dots-num')
        .html('<span class="active">' + pad(i) + '</span>/' + '<span>' + pad(slick.slideCount) + '</span>');
    }).slick({
      dots: true,
      arrows: false,
      slidesToShow: 1,
      slidesToScroll: 1,
      dotsClass: 'slider-dots-list',
      appendDots: programsSliderDots
    });
  }

  if ($('.our-clinic-scheme').length) {
    var dot = $('.our-clinic-scheme').find('.dot');

    dot.each(function(index, el) {
      var ths = $(el),
          dotContent = ths.find('.dot-content');

      ths.on('click', function(event) {
        event.preventDefault();

        dot.find('.dot-content').hide();

        if (!ths.hasClass('active')) {
          ths.addClass('active').siblings().removeClass('active');
          dotContent.fadeIn('fast');
        } else {
          ths.removeClass('active');
        }
      });
    });
  }

  if ($('.img-gallery').length) {
    $('.img-gallery').magnificPopup({
      fixedContentPos: false,
      delegate: 'a',
      type: 'image',
      gallery: {
        enabled: true
      },
      callbacks: {
        open: function() {
          $('body').addClass('gallery-modal');
        },
        close: function() {
          setTimeout(function() {
            $('body').removeClass('gallery-modal');
          }, 200);
        },
      },
    });
  }

  $('a[data-modal]').magnificPopup({
    type: 'inline',
    preloader: false
  });

  // $.magnificPopup.open({
  //   items: {
  //     src: ''
  //   }
  // });

  if ($('.modal-review').length) {
    $('.modal-review').find('.btn-reset').on('click', function(event) {
      event.preventDefault();

      $('.modal-review form')[0].reset();
      $.magnificPopup.close();
    });
  }

});

(function() {
  if (!String.prototype.trim) {
    (function() {
      var rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;
      String.prototype.trim = function() {
        return this.replace(rtrim, '');
      };
    })();
  }

  [].slice.call(document.querySelectorAll('label.styled input, label.styled textarea')).forEach(function(inputEl) {
    if(inputEl.value.trim() !== '') {
      classie.add(inputEl.parentNode, 'focused');
    }

    inputEl.addEventListener('focus', onInputFocus);
    inputEl.addEventListener('blur', onInputBlur);
  });

  [].slice.call(document.querySelectorAll('select.cs-select')).forEach(function(el) {
    new SelectFx(el);
  });

  function onInputFocus(ev) {
    classie.add(ev.target.parentNode, 'focused');
  }
  function onInputBlur(ev) {
    if( ev.target.value.trim() === '' ) {
      classie.remove(ev.target.parentNode, 'focused');
    }
  }
})();


function dynamicPriceTable(service_id, department_id) {
    var x = document.getElementById("toggle");
    var element_for_delete = document.getElementById("dynamic_table");

    $.each(element_for_delete, function(){
      $('#dynamic_table').remove();
    });

        var data = {};
        data.service_id = service_id;
        data.department_id = department_id;

        data["csrfmiddlewaretoken"] = getCookie("csrftoken");
        var url = x.getAttribute('data-view');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
              $.each(data, function(){

                 $('.department-price tbody').append('<tr id="dynamic_table">\n' +
                     '<td>' + this.fields.item_name + '</td>\n' +
                     '<td>' + this.fields.item_price + ' руб.</td>\n' +
                     '<td>' + this.fields.item_time + '</td>\n' +
                     '</tr>');
                 if (x.style.display === "none") {
                     x.style.display = "block";
                 }
              });


            }
        });


}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
