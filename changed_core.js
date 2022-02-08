// 函数名a是自己加进去的
!function () {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) e = Math.random() * b.length, e = Math.floor(e), c += b.charAt(e);
        return c
    }

    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b), d = CryptoJS.enc.Utf8.parse("0102030405060708"),
            e = CryptoJS.enc.Utf8.parse(a), f = CryptoJS.AES.encrypt(e, c, {iv: d, mode: CryptoJS.mode.CBC});
        return f.toString()
    }

    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131), d = new RSAKeyPair(b, "", c), e = encryptedString(d, a)
    }

    function d(d, e, f, g) {
        var h = {}, i = a(16);
        return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
    }

    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d), f
    }

    window.asrsea = d, window.ecnonasr = e
}();

(function () {
    window.NEJ = window.NEJ || {};
    NEJ.O = {};
    NEJ.R = [];
    NEJ.F = function () {
        return !1
    };
    NEJ.P = function (JT1x) {
        if (!JT1x || !JT1x.length) return null;
        var bcH6B = window;
        for (var a = JT1x.split("."), l = a.length, i = a[0] == "window" ? 1 : 0; i < l; bcH6B = bcH6B[a[i]] = bcH6B[a[i]] || {}, i++) ;
        return bcH6B
    };
    NEJ.Q = function (bM8E, JT1x) {
        bM8E = bM8E || NEJ.O;
        var bv8n = JT1x.split(".");
        for (var i = 0, l = bv8n.length; i < l; i++) {
            bM8E = bM8E[bv8n[i]];
            if (!bM8E) break
        }
        return bM8E
    };
    NEJ.C = function () {
        var bBT3x = function () {
            return NEJ.O.toString.call(arguments[0]) != "[object Function]"
        };
        var bBU3x = function (D8v, bD8v) {
            for (var x in bD8v) if (D8v == bD8v[x]) return x;
            return null
        };
        var byz2x = {cy8q: 0, bo8g: 1, bB8t: 2, bW8O: 3, bL8D: 4, fu9l: 5, kI1x: 6, eA9r: 7},
            xF5K = {cD8v: 0, bp8h: 1, bH8z: 2, cg8Y: 3, bT8L: 4, gP0x: 5, lM1x: 6, ge9V: 7};
        return function () {
            var gh0x = function () {
                this.bCC3x();
                return this.cy8q.apply(this, arguments)
            };
            gh0x.prototype.bCC3x = NEJ.F;
            gh0x.prototype.cy8q = NEJ.F;
            gh0x.N8F = function (Fz7s, bDq3x) {
                if (bBT3x(Fz7s)) return;
                if (bDq3x == null || !!bDq3x) NEJ.X(this, Fz7s, bBT3x);
                this.cyV2x = Fz7s;
                this.ct8l = Fz7s.prototype;
                var bK8C = function () {
                };
                bK8C.prototype = Fz7s.prototype;
                this.prototype = new bK8C;
                var GT7M = this.prototype;
                GT7M.constructor = this;
                var cl8d;
                for (var x in byz2x) {
                    cl8d = bBU3x(byz2x[x], xF5K);
                    if (!cl8d || !this.ct8l[x]) continue;
                    GT7M[x] = function (Z8R) {
                        return function () {
                            this[Z8R].apply(this, arguments)
                        }
                    }(cl8d)
                }
                var Ji1x = {};
                for (var x in xF5K) {
                    cl8d = bBU3x(xF5K[x], byz2x);
                    if (!cl8d || !this.ct8l[cl8d]) continue;
                    Ji1x[cl8d] = Fz7s;
                    GT7M[x] = function (Z8R) {
                        return function () {
                            var m7f, bK8C = this.bqB1x[Z8R], biv7o = bK8C.prototype[Z8R];
                            this.bqB1x[Z8R] = bK8C.cyV2x || Fz7s;
                            if (!!biv7o) m7f = biv7o.apply(this, arguments);
                            this.bqB1x[Z8R] = Fz7s;
                            return m7f
                        }
                    }(cl8d)
                }
                GT7M.bCC3x = function () {
                    this.bqB1x = NEJ.X({}, Ji1x)
                };
                GT7M.cQe5j = GT7M.cD8v;
                return GT7M
            };
            return gh0x
        }
    }();
    NEJ.X = function (gK0x, bV8N, ek9b) {
        if (!gK0x || !bV8N) return gK0x;
        ek9b = ek9b || NEJ.F;
        for (var x in bV8N) {
            if (bV8N.hasOwnProperty(x) && !ek9b(bV8N[x], x)) gK0x[x] = bV8N[x]
        }
        return gK0x
    };
    NEJ.EX = function (gK0x, bV8N) {
        if (!gK0x || !bV8N) return gK0x;
        for (var x in gK0x) {
            if (gK0x.hasOwnProperty(x) && bV8N[x] != null) gK0x[x] = bV8N[x]
        }
        return gK0x
    };
    var Ky1x = Function.prototype;
    Ky1x.eN9E = function (lC1x, vy4C) {
        var f = NEJ.F, vy4C = vy4C || f, lC1x = lC1x || f, dE9v = this;
        return function () {
            var d7e = {args: NEJ.R.slice.call(arguments, 0)};
            lC1x(d7e);
            if (!d7e.stopped) {
                d7e.value = dE9v.apply(this, d7e.args);
                vy4C(d7e)
            }
            return d7e.value
        }
    };
    Ky1x.f7c = function () {
        var bm8e = arguments, gK0x = arguments[0], blo9f = this;
        return function () {
            var vw4A = NEJ.R.slice.call(bm8e, 1);
            NEJ.R.push.apply(vw4A, arguments);
            return blo9f.apply(gK0x || window, vw4A)
        }
    };
    Ky1x.eM9D = function () {
        var bm8e = arguments, gK0x = NEJ.R.shift.call(bm8e), blo9f = this;
        return function () {
            NEJ.R.push.apply(arguments, bm8e);
            return blo9f.apply(gK0x || window, arguments)
        }
    };
    var Ky1x = String.prototype;
    if (!Ky1x.trim) {
        Ky1x.trim = function () {
            var dn8f = /(?:^\s+)|(?:\s+$)/g;
            return function () {
                return this.replace(dn8f, "")
            }
        }()
    }
    if (!window.MWF) window.MWF = NEJ;
    if (!window.mwf) window.mwf = NEJ.P("nej");
    if (!window.console) {
        NEJ.P("console").log = NEJ.F;
        NEJ.P("console").error = NEJ.F
    }
    var lt, gt, amp, nbsp, quot, apos, copy, reg
})();

function a() {
    var c7f = NEJ.P
        , ex9o = c7f("nej.g")
        , t7m = c7f("nej.j")
        , j7c = c7f("nej.u")
        , Xp4t = c7f("nm.x.ek")
        , l7e = c7f("nm.x");
    return c7f('dsdadasdasdasdadadasdad.ada.s')
    if (t7m.be8W.redefine)
        return;
    window.GEnc = true;
    var bsR1x = function (cxG2x) {
        var m7f = [];
        j7c.bg8Y(cxG2x, function (cxF2x) {
            m7f.push(Xp4t.emj[cxF2x])
        });
        return m7f.join("")
    };
    var cxE2x = t7m.be8W;
    t7m.be8W = function (Y8Q, e7d) {
        var i7b = {}
            , e7d = NEJ.X({}, e7d)
            , mx2x = Y8Q.indexOf("?");
        if (window.GEnc && /(^|\.com)\/api/.test(Y8Q) && !(e7d.headers && e7d.headers[ex9o.BL6F] == ex9o.FI7B) && !e7d.noEnc) {
            if (mx2x != -1) {
                i7b = j7c.hc0x(Y8Q.substring(mx2x + 1));
                Y8Q = Y8Q.substring(0, mx2x)
            }
            if (e7d.query) {
                i7b = NEJ.X(i7b, j7c.fQ9H(e7d.query) ? j7c.hc0x(e7d.query) : e7d.query)
            }
            if (e7d.data) {
                i7b = NEJ.X(i7b, j7c.fQ9H(e7d.data) ? j7c.hc0x(e7d.data) : e7d.data)
            }

            i7b = {
                csrf_token: "bc5475e560cb2023ad355da57937c2f3",
                op: "add",
                pid: "7273127486",
                trackIds: "[1392141694]",
                tracks: "[object Object]"
            }
            Y8Q = Y8Q.replace("api", "weapi");
            e7d.method = "post";
            delete e7d.query;
            var bVj7c = window.asrsea(JSON.stringify(i7b), bsR1x(["流泪", "强"]), bsR1x(Xp4t.md), bsR1x(["爱心", "女孩", "惊恐", "大笑"]));
            e7d.data = j7c.cq8i({
                params: bVj7c.encText,
                encSecKey: bVj7c.encSecKey
            })
        }
        var cdnHost = "y.music.163.com";
        var apiHost = "interface.music.163.com";
        if (location.host === cdnHost) {
            Y8Q = Y8Q.replace(cdnHost, apiHost);
            if (Y8Q.match(/^\/(we)?api/)) {
                Y8Q = "//" + apiHost + Y8Q
            }
            e7d.cookie = true
        }
        cxE2x(Y8Q, e7d)
    }
    ;
    t7m.be8W.redefine = true
}
