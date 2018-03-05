from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
StoneRadius=.4
NodeRadius=.1

def __main__():


    ###First we define a small lattice
    ###The lattice has the folloing amound if inofmations
    # * Lattice-number
    # * List of Neighbours
    # * Physical positions (x,y)
    # * Ocvupancy: 0=empty,1=white,-1=black
    # * stone visibilty: 0=both,1=only white,-1=only black

    PositionsList=make_board(3,3)    
    LinkList=get_link_list(PositionsList)
    
    print("PositionsList:\n",PositionsList)
    print("LinkList:\n",LinkList)
    [minx,maxx,miny,maxy]=get_min_max(PositionsList)

    plot_lattice(PositionsList,LinkList)
    plot_stones(PositionsList)
    #plt.axis('equal')
    plt.xlim((minx-2,maxx+2))
    plt.ylim((miny-2,maxy+2))
    plt.show(block=False)
    raw_input("Press Enter")

def make_board(nx,ny):
    List=[]
    Nodes=nx*ny
    for ix in range(nx):
        for iy in range(ny):
            id=iy+ix*nx
            ixp=np.mod(iy+(ix+1)*nx,Nodes)
            ixm=np.mod(iy+(ix-1)*nx,Nodes)
            iyp=np.mod(iy+1+(ix)*nx,Nodes)
            iym=np.mod(iy-1+(ix)*nx,Nodes)
            List.append((id,[ixp,ixm,iyp,iym],ix,iy,0,0))
    return List
def plot_stone(PL):
    ax=plt.gcf().gca()
    if PL[4]==0:
        circle = plt.Circle((PL[2], PL[3]), NodeRadius, color='k')
        ax.add_artist(circle)
    elif PL[4]==1:
        circle = plt.Circle((PL[2], PL[3]), StoneRadius, color='grey')
        ax.add_artist(circle)
        circle = plt.Circle((PL[2], PL[3]), StoneRadius, color='k',fill=False)
        ax.add_artist(circle)
    elif PL[4]==-1:
        circle = plt.Circle((PL[2], PL[3]), StoneRadius, color='k')
        ax.add_artist(circle)
    plt.text(PL[2], PL[3],str(PL[0]),color='r')
        
def plot_stones(PList):
    [ plot_stone(PL) for PL in PList]
    
def get_min_max(PList):
    minx=np.min([PL[2] for PL in PList])
    miny=np.min([PL[3] for PL in PList])
    maxx=np.max([PL[2] for PL in PList])
    maxy=np.max([PL[3] for PL in PList])
    return minx,maxx,miny,maxy
    

def get_link_list(PList):
    from itertools import chain
    return list(chain.from_iterable([ [ (PX[0],y) for y in PX[1]] for PX in PList]))

def plot_lattice(PList,Llist):
    [minx,maxx,miny,maxy]=get_min_max(PList)
    DeltaX=maxx-minx+1
    DeltaY=maxy-miny+1
    [ plot_line(PList[L[0]],PList[L[1]],DeltaX,DeltaY) for L in Llist]

def plot_line(P1,P2,DX,DY):
    V1=np.array([P1[2],P1[3]])
    V2List=[np.array([P2[2],P2[3]])
     ,np.array([P2[2],P2[3]+DY])
     ,np.array([P2[2],P2[3]-DY])
     ,np.array([P2[2]+DX,P2[3]])
     ,np.array([P2[2]+DX,P2[3]+DY])
     ,np.array([P2[2]+DX,P2[3]-DY])
     ,np.array([P2[2]-DX,P2[3]])
     ,np.array([P2[2]-DX,P2[3]+DY])
     ,np.array([P2[2]-DX,P2[3]-DY])]
    #print("V2List:",V2List)
    DistNo=np.argmin([np.linalg.norm(V1-V2) for V2 in V2List])
    plt.plot((V1[0],V2List[DistNo][0]),(V1[1],V2List[DistNo][1]),'-k')
    
if __name__ == '__main__' :
    __main__()
