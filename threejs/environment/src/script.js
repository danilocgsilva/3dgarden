import './style.css'
import * as THREE from 'three'
import SceneBuilder from './building_environment/SceneBuilder'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'

const canvas = document.querySelector('canvas.webgl')
const sceneBuilder = new SceneBuilder()
sceneBuilder.setTorus()
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}
sceneBuilder.setCamera(sizes)
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
const camera = sceneBuilder.exposeCamera()
const controls = new OrbitControls( camera, renderer.domElement );
const scene = sceneBuilder.exposeScene()
const tick = () =>
{
    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
}
tick()
window.addEventListener('resize', () =>
{
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight

    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()

    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})