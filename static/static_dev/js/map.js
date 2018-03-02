var myPlacemark = [];
ymaps.ready(function () {
    var myMap;
    myMap = document.getElementById('map');
    myMap = new ymaps.Map(myMap, {
        center: [57.80799947186481,28.353194037082265],
        zoom: 17,
        controls: []
    });

    myMap.controls.add('zoomControl', {
        position: {top: 100, left: 15}
    });
    myMap.behaviors.disable('scrollZoom');

    var myBalloonLayout = ymaps.templateLayoutFactory.createClass(
        '<div class="balloon-layout">' +
        '<span class="close">&times;</span>' +
        '$[[options.contentLayout observeSize minWidth=200 maxWidth=200]]' +
        '<div class="balloon-arrow"></div>' +
        '</div>', {
            build: function () {
                this.constructor.superclass.build.call(this);
                this._$element = $('.balloon-layout', this.getParentElement());
                this.applyElementOffset();
                this._$element.find('.close').on('click', $.proxy(this.onCloseClick, this));
            },
            clear: function () {
                this._$element.find('.close').off('click');
                this.constructor.superclass.clear.call(this);
            },
            onSublayoutSizeChange: function () {
                myBalloonLayout.superclass.onSublayoutSizeChange.apply(this, arguments);
                if(!this._isElement(this._$element)) {
                    return;
                }
                this.applyElementOffset();
                this.events.fire('shapechange');
            },
            applyElementOffset: function () {
                this._$element.css({
                    left: -(this._$element[0].offsetWidth),
                    top: -(this._$element[0].offsetHeight + 20)
                });
            },
            onCloseClick: function (e) {
                e.preventDefault();
                this.events.fire('userclose');
            },
            getShape: function () {
                if(!this._isElement(this._$element)) {
                    return MyBalloonLayout.superclass.getShape.call(this);
                }
                var position = this._$element.position();
                return new ymaps.shape.Rectangle(new ymaps.geometry.pixel.Rectangle([
                    [position.left, position.top], [
                        position.left + this._$element[0].offsetWidth,
                        position.top + this._$element[0].offsetHeight + this._$element.find('.balloon-arrow')[0].offsetHeight
                    ]
                ]));
            },
            _isElement: function (element) {
                return element && element[0] && element.find('.balloon-arrow')[0];
            }
        }
    );

    var myBalloonContentLayout = ymaps.templateLayoutFactory.createClass(
        '<div class="ballon-content">$[properties.balloonContent]</div>'
    );

    var org_info = [];
    // x - C
    // y - ll
    org_info[0] = [];
    org_info[0]['geo_coord_x'] = 57.80799947186481;
    org_info[0]['geo_coord_y'] = 28.353194037082265;
    org_info[0]['text'] = '<p>ООО «Клиника» <br /> 180004, Псков, ул. Бастионная, д. 9</p><p>&nbsp;</p><p><b>8 (8112) 44-03-03</b></p><p>info@clinicmedica.ru</p>';

    var html;
    for(i = 0; i < org_info.length; i++) {

        html = '<div class="balloon" balloon-num="'+i+'" onClick="close_balloon(this)">';

        html += '<div class="story">' + org_info[i]['text'] + '</div>';
        // html += '<span class="balloon" onClick="close_balloon(this)" balloon-num="'+i+'"></span>';

        html += '</div>';

        myPlacemark[i] = new ymaps.Placemark([org_info[i]['geo_coord_x'], org_info[i]['geo_coord_y']], {
            balloonContent: html
        }, {
            iconLayout:'default#image',
            iconImageHref: 'images/map-pin.png',
            iconImageSize: [40, 50],
            iconImageOffset: [-20, -50],
            balloonLayout: myBalloonLayout,
            balloonContentLayout: myBalloonContentLayout,
        });

        myMap.geoObjects.add(myPlacemark[i]);
    }
});

function close_balloon(obj) {
    var id = $(obj).attr('balloon-num');
    myPlacemark[id].balloon.close();
}
