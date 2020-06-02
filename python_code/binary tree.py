from graphviz import Digraph
import pygraphviz as pgv
# from graphviz import Digraph
# dot = Digraph(comment='The Test Table')
# # 添加圆点A,A的标签是Dot A
# dot.node('A', 'D1')
# dot.node('B', 'D2')
# dot.node('C', 'D3')
# dot.node('-6', '${D_{-6}}$')
# dot.node('-5', '${D_{-5}}$')
# dot.node('-4', '${D_{-4}}$')
# dot.node('-3', '${D_{-3}}$')
# dot.node('-2', '${D_{-2}}$')
# dot.node('-1', '${D_{-1}}$')
# dot.node('0', '${D_{0}}$')
# dot.node('1', '${D_{1}}$')
# dot.node('2', '${D_{2}}$')
# dot.node('3', '${D_{3}}$')
# dot.node('5', '${D_{5}}$')
# dot.node('6', '${D_{6}}$')
# dot.node('7', '${D_{7}}$')
# dot.node('8', '${D_{8}}$')
# dot.node('9', '${D_{0}}$')

# dot.edges(['AB'])
# # dot.view()
# # 在创建两圆点之间创建一条边
# dot.edge('B', 'C', 'test')
# # dot.view()
# # 获取DOT source源码的字符串形式
# print(dot.source)
# dot.view()
# dot.render('test-table.gv', view=True)




g=pgv.AGraph()  #建立图
g.add_node('-1')  #建立点
g.add_edge('-1','6')  #建立边
g.add_edge('-1','5')  #建立边
g.add_edge('6','7')  #建立边
g.add_edge('7','8')  #建立边
g.add_edge('7','3')  #建立边
g.add_edge('5','0')  #建立边
g.add_edge('0','-2')  #建立边
g.add_edge('-2','4')  #建立边
g.add_edge('-2','-3')  #建立边
g.add_edge('-3','-4')  #建立边
g.add_edge('-3','-9')  #建立边
g.add_edge('-9','-8')  #建立边
g.add_edge('-8','-7')  #建立边
g.add_edge('-7','-6')  #建立边
g.add_edge('-6','-5')  #建立边


g.layout(prog='dot')  #绘图类型
g.draw('pyg1.png')   #绘制