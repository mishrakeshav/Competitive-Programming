#include <bits/stdc++.h>
using namespace std;
//#define che
#define debug(...) fprintf(stderr,__VA_ARGS__)
#define MK make_pair
#define PB push_back
#define fi first
#define se second

typedef long long LL;
typedef pair<int, int> PII;
const int N=5e4+10, dx[4]={0,-1, 0, 1}, dy[4]={1,0,-1,0}; // ri, up, lf, dw; E, N, W, S
map<PII, PII> lf, ri, dw, up;
set<PII> occr;
char s[N];
int n,r,c;
PII cur;



PII near(PII a, int dr){return MK(a.fi+dx[dr], a.se+dy[dr]);}
bool legal(PII a){return 1<=a.fi && a.fi<=r && 1<=a.se && a.se<=c;}
PII jump(PII u,map<PII, PII> &fa){
	return fa.count(u) ? fa[u]=jump(fa[u], fa) : u;
}
int main(){
	#ifdef che
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	#endif
	int Tes;scanf("%d", &Tes);
	for (int T=1; T<=Tes; ++T){
		lf.clear(); ri.clear(); dw.clear(); up.clear();occr.clear();	
		scanf("%d%d%d%d%d", &n, &r, &c, &cur.fi, &cur.se);
		occr.insert(cur);
		scanf("%s",s);
		for (int i=0; i<n; ++i){
			PII nx=cur,nr;
			if ( s[i]=='E'){
				if ( ri.count(cur)){nx=jump(cur, ri);}
				nx=near(nx,0);
			}else
			if ( s[i]=='N'){
				if ( up.count(cur)){nx=jump(cur, up);}
				nx=near(nx,1);
			}else
			if ( s[i]=='W'){
				if ( lf.count(cur)){nx=jump(cur, lf);}
				nx=near(nx,2);
			}else
			if ( s[i]=='S'){
				if ( dw.count(cur)){nx=jump(cur, dw);}
				nx=near(nx,3);
			}
			
			cur=nx;
			occr.insert(cur);
			#ifdef che
			debug("i=%d, dir=%c, cur=(%d,%d)\n", i, s[i], cur.fi, cur.se);
			#endif
			nr= near(cur,0);
			if ( legal(nr) && occr.count(nr)) ri[cur]=nr,lf[nr]=cur;

			nr= near(cur,1);
			if ( legal(nr) && occr.count(nr)) up[cur]=nr,dw[nr]=cur;
			nr= near(cur,2);
			if ( legal(nr) && occr.count(nr)) lf[cur]=nr,ri[nr]=cur;
			nr= near(cur,3);
			if ( legal(nr) && occr.count(nr)) dw[cur]=nr,up[nr]=cur;
			#ifdef che
			if ( cur==MK(1,2)) debug("nr=(%d,%d), occr.count()=%d\n", nr.fi, nr.se, occr.count(cur));
			#endif
			
		}
		printf("Case #%d: %d %d\n",T, cur.fi, cur.se);
	}
	return 0;
}