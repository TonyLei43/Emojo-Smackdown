(() => {
    "use strict";
    var e, r = {},
        o = {};

    function t(e) {
        var n = o[e];
        if (void 0 !== n) return n.exports;
        var i = o[e] = {
            id: e,
            loaded: !1,
            exports: {}
        };
        return r[e].call(i.exports, i, i.exports, t), i.loaded = !0, i.exports
    }
    t.m = r, t.amdD = function() {
        throw new Error("define cannot be used indirect")
    }, t.amdO = {}, e = [], t.O = (r, o, n, i) => {
        if (!o) {
            var a = 1 / 0;
            for (c = 0; c < e.length; c++) {
                for (var [o, n, i] = e[c], l = !0, s = 0; s < o.length; s++)(!1 & i || a >= i) && Object.keys(t.O).every((e => t.O[e](o[s]))) ? o.splice(s--, 1) : (l = !1, i < a && (a = i));
                if (l) {
                    e.splice(c--, 1);
                    var d = n();
                    void 0 !== d && (r = d)
                }
            }
            return r
        }
        i = i || 0;
        for (var c = e.length; c > 0 && e[c - 1][2] > i; c--) e[c] = e[c - 1];
        e[c] = [o, n, i]
    }, t.n = e => {
        var r = e && e.__esModule ? () => e.default : () => e;
        return t.d(r, {
            a: r
        }), r
    }, t.d = (e, r) => {
        for (var o in r) t.o(r, o) && !t.o(e, o) && Object.defineProperty(e, o, {
            enumerable: !0,
            get: r[o]
        })
    }, t.g = function() {
        if ("object" == typeof globalThis) return globalThis;
        try {
            return this || new Function("return this")()
        } catch (e) {
            if ("object" == typeof window) return window
        }
    }(), t.o = (e, r) => Object.prototype.hasOwnProperty.call(e, r), t.r = e => {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }, t.nmd = e => (e.paths = [], e.children || (e.children = []), e), (() => {
        var e = {
            666: 0
        };
        t.O.j = r => 0 === e[r];
        var r = (r, o) => {
                var n, i, [a, l, s] = o,
                    d = 0;
                if (a.some((r => 0 !== e[r]))) {
                    for (n in l) t.o(l, n) && (t.m[n] = l[n]);
                    if (s) var c = s(t)
                }
                for (r && r(o); d < a.length; d++) i = a[d], t.o(e, i) && e[i] && e[i][0](), e[a[d]] = 0;
                return t.O(c)
            },
            o = self.webpackChunkrock_paper_scissors = self.webpackChunkrock_paper_scissors || [];
        o.forEach(r.bind(null, 0)), o.push = r.bind(null, o.push.bind(o))
    })()
})();